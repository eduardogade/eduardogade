
class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1231456718910
                |  |

         |     |
        1231456718910
           |     |

        1 | 23145671891 | 0
        1 | 231 | 45671 | 891 | 0

        2314567

        122333444455555
           ||
        """

        # Initialization
        max_len: int = 0
        total_len: int = len(s)
        final_max_len: int = 0

        # Initial check
        if total_len == 0:
            return total_len
        if total_len == 1:
            return total_len

        # Structure initialization
        h: dict[str, int] = dict({"$": -1})
        si: int = -1
        ei: int = 0

        # Helper
        def _g(i: int) -> str:
            if i < 0:
                return "$"
            return s[i]

        # def _hg(i: int) -> tuple[int | None, int | None]:

        #     hhi = h.get(ev, None)
        #     if hhi is None:
        #         return None, None
        #     return hhi[0], len(hhi)

        # def _hp(i: int, symb: str) -> None:
        #     try:
        #         h[symb].append(i)
        #     except Exception:
        #         h[symb] = [i]

        counter = 1
        while True:

            print(f"Iteration = {counter}")

            sv: str = _g(si)
            ev: str = _g(ei)
            hi: int | None = h.get(ev, None)
            eqv: bool = sv == ev
            eqh: bool = hi is not None
            print(f"IDX1:\tsi = {si} | ei = {ei} | hi = {hi}")
            print(f"VAL1:\tsv = {sv} | ev = {ev} | hv = {ev}")
            print(f"EQLEN1:\teqv = {eqv} | eqh = {eqh}")
            print(f"FLEN1:\tmax_len = {max_len} | final_max_len = {final_max_len}")
            print(f"HDIC1:\th = {h}")
            print(f"{'-'*20}")

            # Main check
            if eqv or eqh:

                is_dollar = h.get("$", None) is not None

                l_hs = hi - si - 1 if is_dollar else hi - si
                l_eh = ei - hi
                l_es = ei - si - 1 if is_dollar else ei - si
                max_len = max(l_hs, l_eh, l_es, max_len)
                final_max_len = max(final_max_len, max_len)
                print(f"LEN3:\tl_hs = {l_hs} | l_eh = {l_eh} | l_es = {l_es}")
                print(f"FLEN3:\tmax_len = {max_len} | final_max_len = {final_max_len}")
                print(f"{'-'*20}")

                si = hi + 1
                ei = si + 1
                h = {_g(si): si}

                max_len = 1
                counter += 1

                print(f"IDX3:\tsi = {si} | ei = {ei} | hi = {hi}")
                print(f"VAL3:\tsv = {sv} | ev = {ev} | hv = {ev}")
                print(f"FLEN4:\tmax_len = {max_len} | final_max_len = {final_max_len}")
                print(f"HDIC3:\th = {h}")
                print(f"{'-'*30}\n")
                if final_max_len > total_len - si or ei >= total_len:
                    return final_max_len

                continue

            h[ev] = ei
            ei += 1

            max_len += 1

            if ei >= total_len:
                final_max_len = max(final_max_len, max_len)
                return final_max_len

            print(f"IDX2:\tsi = {si} | ei = {ei} | hi = {hi}")
            print(f"VAL2:\tsv = {sv} | ev = {ev} | hv = {ev}")
            print(f"FLEN2:\tmax_len = {max_len} | final_max_len = {final_max_len}")
            print(f"HDIC2:\th = {h}")
            print(f"{'-'*30}\n")
            counter += 1

if __name__ == "__main__":

    s = Solution()
    # res = s.lengthOfLongestSubstring(s="")
    # res = s.lengthOfLongestSubstring(s="a")
    # res = s.lengthOfLongestSubstring(s="aa")
    # res = s.lengthOfLongestSubstring(s="ab")
    # res = s.lengthOfLongestSubstring(s="aaaaaaaaaa")
    # res = s.lengthOfLongestSubstring(s="abcabcbb")
    # res = s.lengthOfLongestSubstring(s="abbcccddddeeeee")
    # res = s.lengthOfLongestSubstring(s="abcadefgahiaj") # 7
    res = s.lengthOfLongestSubstring(s="dvdf") # 3
    print(f"res = {res}")
