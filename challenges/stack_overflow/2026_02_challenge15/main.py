# SPDX-License-Identifier: MIT
# main.py
"""
StackOverflow Challenges | Alien Dictionary | Main
==================================================

Metadata
--------
- Project: StackOverflow Challenges
- License: MIT
"""


# -------------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------------
from __future__ import annotations

import argparse
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Final, Sequence, DefaultDict


# -------------------------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------------------------
# Common "invisible" troublemakers you may want to treat explicitly.
_BOMS: Final[tuple[str, ...]] = (
    "\ufeff",  # UTF-8 BOM *as decoded text*, also used in UTF-16/32 decoded contexts
)

_LINE_SEPARATORS: Final[tuple[str, ...]] = (
    "\r\n", "\n", "\r",          # usual
    "\u2028", "\u2029",          # Unicode line/paragraph separators
)

TRUE_VALUE_SET: set[str] = {"true", "t", "yes", "y", "1", "on"}

FALSE_VALUE_SET: set[str] = {"false", "f", "no", "n", "0", "off"}


# -------------------------------------------------------------------------------------
# CLI
# -------------------------------------------------------------------------------------
def _as_path(value: str) -> Path:
    """
    Convert a path-like string into a deterministic Path.

    Rules (strict)
    --------------
    - Expands "~" to the user home directory.
    - If the path is relative, it is ALWAYS anchored to the current working directory.
    - No project-relative or caller-relative behavior.
    - Optional filesystem resolution via `resolve=True`.

    This function is deterministic with respect to:
      - input string
      - current working directory

    Parameters
    ----------
    value : str
        Path string (absolute or relative).
    resolve : bool, optional
        If True, call `.resolve()` (normalizes ".."/"." and resolves symlinks).
        Default is False.

    Returns
    -------
    Path
        Deterministic Path object.
    """
    p = Path(value).expanduser()

    if not p.is_absolute():
        p = Path.cwd() / p

    return p.resolve()

def _as_bool(value: str) -> bool:
    """
    Convert a bool-like string into a python boolean.

    Rules
    -----
    True: '

    Parameters
    ----------
    value : str
        Path string (absolute or relative).

    Raises
    ------
    Raises argparse.ArgumentTypeError on invalid values.

    Returns
    -------
    bool
        The corresponding True or False.
    """
    v = value.strip().lower()
    if v in TRUE_VALUE_SET:
        return True
    if v in FALSE_VALUE_SET:
        return False
    raise argparse.ArgumentTypeError(
        f"Invalid boolean value: {value!r}. Use one of: \n"
        f"  - True Values: {", ".join(sorted(TRUE_VALUE_SET))}\n"
        f"  - False Values: {", ".join(sorted(FALSE_VALUE_SET))}\n"
    )

def _build_parser() -> argparse.ArgumentParser:
    """Builds parser"""
    p = argparse.ArgumentParser(
        prog="challenge15",
        description=(
            "\nchallenge15 | Alien Dictionary solver (robust I/O + ordering)\n\n"
            "By: Eduardo gade Gusmao | eduardo@gusmaolab.org\n"
            "\n"
            "This implementation uses a seed-aware Kahn's algorithm:\n"
            "1. Initialize vertices\n"
            "2. Build edges from adjacent words\n"
            "3. Topological sort (Kahn)\n"
            "4. Cycle detection\n"
            "\n"
            "Seed-Aware Behavior: Topological sorting is not necessarily unique.\n"
            "When multiple symbols are eligible (indegree zero), this implementation\n"
            "can be made deterministic by seeding the selection order (e.g., sorting\n"
            "candidates or using a stable tie-breakrule). A deterministic tie-break\n"
            "makes results reproducible across runs, which is often useful for\n"
            "testing and for downstream pipelines.\n"
            "\n"
            "Overall time complexity: O(C + V + E).\n"
        ),
        epilog=(
            "$ python challenge_15.py --help\n"
            "$ python challenge_15 ./input/original-so.txt\n"
            "$ python challenge_15 ./input/original-so "
            "-o ./output/original-so.txt\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    p.add_argument("--version", action="version", version="0.1.1")

    p.add_argument(
        "input_path",
        type=_as_path,
        metavar="PATH",
        help="Input file containing the dictionary words (one per line).",
    )

    p.add_argument(
        "-o",
        "--output-path",
        dest="output_path",
        type=_as_path,
        default=None,
        metavar="PATH",
        help="Optional output path for the ordered alphabet and statistics.",
    )

    p.add_argument(
        "-d",
        "--deterministic",
        dest="deterministic",
        type=_as_bool,
        default="T",
        metavar="T | F",
        help=(
            "Optional seed for reproducibility testing - If set to 'true'"
            " the topological sorting will be stable using a heap approach. "
            "Otherwise, it does rely solely on pythons deque insertion order."
        ),
    )

    return p


# -------------------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------------
def main(argv: Sequence[str] | None = None) -> int:
    """
    """
    # Part 1 - Reading arguments
    argv = sys.argv[1:] if argv is None else list(argv)
    args = _build_parser().parse_args(argv)

    # Part 2 - Treating data
    words, stats = _read_words_robust(args.input_path)

    # Part 3 - Performing Alien Dictionary Ordering
    order: list[str] | None
    if args.deterministic:
        order = alien_order_robust_deterministic(words)
    else:
        order = alien_order_robust(words)

    # Part 4 - Making Pyright happy
    if order is not None:
        order = [str(e) for e in order if e]
    else:
        order = []

    # Part 5 - Writing output to the desired location
    to_write: list[str] = []
    to_write.append(f"# Ordered sequence:\n{''.join(order)}\n\n")
    to_write.append(f"# Encoding of the file: {stats.encoding_used}\n")
    to_write.append(f"# Total number of lines: {stats.total_lines}\n")
    to_write.append(f"# Number of lines used: {stats.kept_lines}\n")
    to_write.append(f"# Number of lines cleaned out: {stats.skipped_empty_or_ws}\n")
    to_write.append(
        f"# Set of unique symbols (non-ordered): "
        f"{{{', '.join(stats.unique_symbols)}}}\n\n"
    )
    to_write.append(f"{'-'*50}\n\n")

    if args.output_path is None:
        # print to stdout
        sys.stdout.write(f"{''.join(to_write)}")
    else:
        args.output_path.parent.mkdir(parents=True, exist_ok=True)
        args.output_path.write_text(f"{''.join(to_write)}", encoding="utf-8")

    # Return success
    return 0


# --------------------------------------------------------------------------------------
# Exports
# --------------------------------------------------------------------------------------
__all__: list[str] = [
    "main",
]


# -------------------------------------------------------------------------------------
# Test | python challenge_15.py input-utf8.txt > out.txt 2>&1
# -------------------------------------------------------------------------------------
if __name__ == "__main__":
    raise SystemExit(main())
