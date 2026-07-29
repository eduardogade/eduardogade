"""
file reader
   ↓
parse row
   ↓
filter ERROR logs
   ↓
store results

PIPELINE MENTAL MODEL

O:  source
      ↓
DE: decode
      ↓
C:  clean
      ↓
T: transform
      ↓
A: aggregate
      ↓
S:  sink

O | DE | C | T | A | S

EXAMPLE IN GENOMICS:

FASTQ reader
   ↓
quality filter
   ↓
adapter trimming
   ↓
alignment
   ↓
variant calling


Why Interviewers Care:

RL1: S3 → Spark → Delta Lake

RL2: Kafka → Flink → Warehouse


Iterable vs Iterator vs Generator

Iterable: An object you can loop over.
Example:
list[int]
str
dict[str, int]
set[int]
range
generator
Implements: __iter__()

Iterator: An object that produces the next value one by one.
Example: Generators
Implements: __iter__() and __next__()

- every iterator is iterable
- not every iterable is an iterator


Here is the clean verbal explanation:
An iterable is anything you can loop over. An iterator is the object that actually
yields values one at a time via next(). Generators are a convenient way to build
iterators lazily, which makes them ideal for streaming-style data pipelines in Python.


Data Streaming:

A streaming read means consuming data increamentally,
without loading the entire dataset into memory.

Streaming Read:
A read pattern where the data is consumed "pice by piece":
- Line by line
- row by row
- chunk by chunk
- message by message
- page by page

2. Why Using It:
- Datasets are too large for RAM
- arrive continuously
- are in remote locations
- are compressed
- are partially invalid
- needed by downstream consumers immediately

Streaming helps with:
-> Lower memory pressure.
-> Faster time-to-first-result.
-> Better pipeline composability: reader -> parser -> validator -> writer
-> Better operational behavior

3. In Python

A. Line-by-line text file reading
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        yield line.rstrip("\n")

B. Fixed-size chunk reads
with open(path, "rb") as f:
    while chunk := f.read(8192):
        yield chunk

C. CSV row streaming
import csv

with open(path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        yield row

D. API/page streaming
page = 1
while True:
    rows = fetch_page(page)
    if not rows:
        break
    for row in rows:
        yield row
    page += 1

4. Record stream vs byte stream

Byte Stream: Tread the bytes with `f.read(8192)`

Record Stream: You read meaningul logical units

5. The most common mistake: accidental de-streaming

Within the middle of a nice stream you load the whole
object.

E.g. `list()` in the middle of the pipeline can collapse
the whole system.


6. Streaming reads and validation

def parse_rows(lines):
    for idx, line in enumerate(lines, start=1):
        try:
            yield parse(line)
        except ValueError as e:
            log_bad_row(idx, line, e)
            continue

If downstream is slow:
- database writes
- API calls
- model inference
- disk output

then upstream must not flood memory.

8. Streaming reads with batching

source → parse → filter → batch → sink

O:  source
      ↓
PE: parse
      ↓
F:  filter
      ↓
BA: batch
      ↓
S:  sink


10. Streaming compressed data

import gzip

with gzip.open(path, "rt", encoding="utf-8") as f:
    for line in f:
        yield line

11. Streaming reads in omics / life sciences thinking
Without going deep into domain tooling yet, the principle maps directly.

- FASTQ records processed sequentially
- VCF lines parsed one at a time
- metadata manifests streamed row-wise
- giant phenotype CSV/TSV files ingested incrementally

12. Streaming read patterns you should be able to describe in an interview
You do not need theatrical wording. Just say it plainly.

For large datasets I prefer streaming ingestion patterns —
line-by-line or row-by-row reads,
immediate validation and transformation,
then batching for sink writes.
That keeps memory bounded and makes fault handling more localized.

13. When streaming is not the right choice
You may choose full materialization when:
- dataset is genuinely small
- you need random access
- you need global sorting
- you need full-table joins in memory
- vectorized dataframe operations are clearly better

14. The progression you should now see

Pipeline pattern
General “flow through stages” mental model

Generators
Lazy stage construction

Iterators
Underlying mechanics and single-pass behavior

Streaming reads
Real ingestion patterns in production-ish code


15. Final interview-ready synthesis for this topic

If they ask something like:
“How do you think about Python data pipelines for large files?”

A strong compact answer is:
I try to keep the pipeline streaming-friendly:
read incrementally,
parse lazily,
validate per record,
filter early,
and only batch where batching improves sink efficiency.
In Python that usually means iterables, generators, and chunked or row-wise reads
instead of materializing everything into memory.

"""

# from pathlib import Path
# from typing import Generator

# import pandas as pd

# def transform(ds: pd.Series) -> pd.Series:
#     out: pd.Series
#     return out
# def write_row(ds: pd.Series) -> None.

# def main(input_path: Path) -> int:
#     iterator: pd.Series | None = None
#     for iterator in pd.read_csv_stream(input_path):
#         row = transform(row)
#         write_row(row)
#     return 0

# def read_lines(path: str) -> Generator[str, None, None]:
#     with open(path) as f:
#         for line in f:
#             yield line.strip()
# def parse_line(line: str):
#     date, level, message = line.split(",", 2)
#     return {"date": date, "level": level, "message": message}
# def filter_errors(records: str) -> Generator[str, None, None]:
#     records: pd.Series = pd.read_csv_stream()
#     for record in records:
#         if record["entry"] == "ERROR":
#             yield record
# for error in errors:
#     print(error)

# Exercise 1

# def read_lines(path: Path) -> Generator[str, None, None]:
#     idx: int = 0
#     with open(path, "r", encoding="utf-8") as f:
#         try:
#             for idx, line in enumerate(f, start=1):
#                 yield line.strip()
#         except Exception as e:
#             print(f"Error at line {idx}: {e}")

# def read_chars(line: str) -> Generator[int, None, None]:
#      for idx, c in enumerate(line, start=1):
#         try:
#             yield ord(c)
#         except Exception as e:
#             print(f"Error at line {idx}: {e}")

# def filter_line(line_int: int) -> bool:
#     if line_int%2==0:
#         return True
#     return False

# def print_line(input_path: Path) -> None:
#     for line_str in read_lines(input_path):
#         if filter_line(sum(read_chars(line_str))):
#             print(line_str)

# if __name__ == "__main__":
#     root: Path = Path("/Users/egg/projects/eduardogade/scripts/")
#     input_path: Path = root / "exercise_1.txt"
#     lines = print_line(input_path)

# Exercise 3

# def read_lines(path: Path) -> Generator[str | None, None, None]:
#     with open(path, "r", encoding="utf-8") as f:
#         for idx, line in enumerate(f, start=1):
#             try:
#                 yield line.strip()
#             except Exception as e:
#                 print(f"Error at line {idx}: {e}")
#                 yield None

# def read_chars(line: str | None) -> int | None:
#     if isinstance(line, str):
#         try:
#             return int(line)
#         except Exception as e:
#             print(f"Error at line {line}: {e}")
#             return None
#     return None

# def filter_line(line_int: int | None) -> int | None:
#     if isinstance(line_int, int):
#         if line_int > 10:
#             return line_int
#         return None
#     return None

# def print_line(input_path: Path) -> None:
#     for line_str in read_lines(input_path):
#         line_int: int | None = read_chars(line_str)
#         if line_int is not None:
#             filtered: int | None = filter_line(line_int)
#             if filtered is not None:
#                 print(filtered)

# NUM_COLS = 5

# def read_lines(path: Path) -> Generator[str | None, None, None]:
#     with open(path, "r", encoding="utf-8") as f:
#         for idx, line in enumerate(f, start=1):
#             try:
#                 yield line.strip()
#             except Exception as e:
#                 print(f"Error at line {idx}: {e}")
#                 yield None

# def parse_int(line: str | None) -> Generator[int | None, None, None]:
#     def _valid(line_list: list[str]) -> bool:
#         if len(line_list) == 5:
#             return True
#         return False
#     if isinstance(line, str):
#         line_list: list[str] = line.split("\t")
#         if _valid(line_list):
#             for element in line_list:
#                 try:
#                     yield int(element)
#                 except Exception:
#                     pass
#     return None

# def filter_even(nums: list[int]) -> Generator[int | None, None, None]:
#     for element in nums:
#         if element%2 == 0:
#             yield element
#         yield None
#     return None

# def batched(nums: list[int], *, batch_size: int = 3) -> Generator[list[int] | None, None, None]:
#     batch: list[list[int]] = []
#     flag_first = True
#     for element in nums:
#         if flag_first:
#             flag_first = False
#             batch.append([element])
#         else:
#             batch[-1].append(element)
#         if len(batch) == batch_size:
#             flag_first = True
#             yield batch[-1]
#             batch = []
#     if batch and not flag_first:
#         yield batch[-1]
#     return None

# def print_line(input_path: Path) -> None:
#     for line_str in read_lines(input_path):
#         line_int: int | None = parse_int(line_str)
#         if line_int is not None:
#             filtered: int | None = filter_even(line_int)
#             if filtered is not None:
#                 batch: list[int] | None = batched(filtered)
#                 if batch is not None:
#                     print(batch)


# from collections.abc import Iterator, Iterable, Generator
# from pathlib import Path
# from typing import TextIO

# class ReadNumbers(Iterator[int]):

#     def __init__(self, input_path: Path):
#         self.input_path : Path = input_path
#         self.file: TextIO = open(self.input_path, "r", encoding="utf-8")

#     def __iter__(self) -> "ReadNumbers":
#         return self

#     def __next__(self) -> int:
#         if isinstance(g := self._generating(), str):
#             if isinstance(t := self._transform(g), int):
#                 if isinstance(f := self._filter(t), int):
#                     return f
#         return -1

#     def _generating(self) -> Generator[str | None, None, None]:
#         try:
#             yield self.file.readline().strip()
#         except Exception:
#             pass
#         return None

#     def _transform(self, line: str | None) -> int | None:
#         if isinstance(line, str):
#             try:
#                 return int(line)
#             except Exception:
#                 return None
#         return None

#     def _filter(self, num: int | None) -> int | None:
#         if isinstance(num, int):
#             try:
#                 if num % 2 == 0:
#                     return num
#                 return None
#             except Exception:
#                 return None
#         return None


# def parse_ints(lines: Iterable[str]) -> Iterator[int]:
#     for line in lines:
#         try:
#             yield int(line)
#         except ValueError:
#             continue

# class CountUpTo(Iterator[int]):
#     def __init__(self, limit: int) -> None:
#         self.current = 1
#         self.limit = limit

#     def __iter__(self) -> "CountUpTo":
#         return self

#     def __next__(self) -> int:
#         if self.current > self.limit:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value


if __name__ == "__main__":
    root: Path = Path("/Users/egg/projects/eduardogade/scripts/")
    input_path: Path = root / "numbers.txt"
    print_line(input_path)



