"""

Code
Testcase
Testcase
Test Result
5. Longest Palindromic Substring
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.


I just need a Walrus LIFO

LIFO Example:

String: aabccddeddccdda
Solution (by eye): ccddeddcc
Each round the pipe symbol show where we are on the string and the LIFO + Hashmap

Round 1: Put a in the LIFO and move.
aabccddeddccdda
|
LIFO: ..
      ||

Round 2: Next a matches the a in the LIFO, so we enter "palindro-mode" ON. Plus, I put "b" in the LIFO.
aabccddeddccdda
 |
LIFO: a.
      ||

Round 3: Next char b does not match first/second LIFO char, so panlindro-mode OFF (largest so far "aa") and I put b in LIFO.
aabccddeddccdda
  |
LIFO: aa
      ||

Round 3: Next char c does not match first/second LIFO char, so panlindro-mode OFF (largest so far "aa") and I put c in LIFO.
aabccddeddccdda
   |
LIFO: baa
      ||

Round 4: Next char c does MATCH first/second LIFO char, so panlindro-mode ON and I put c in LIFO.
aabccddeddccdda
    |
LIFO: cbaa
      ||

Round 5: Next char d does not match first/second LIFO char, so panlindro-mode OFF (largest so far "cc") and I put d in LIFO.
aabccddeddccdda
     |
LIFO: ccbaa
      ||

Next ones I will do just the steps because I am tired:

Round 6:
aabccddeddccdda
      |
LIFO: dccbaa
      ||

Round 7: max = dd
aabccddeddccdda
       |
LIFO: ddccbaa
      ||

Round 6:
aabccddeddccdda
       |
LIFO: ddccbaa
      ||

Round 7: ON
aabccddeddccdda
        |
LIFO: eddccbaa
      ||

Round 8: Madonna-ing the walrus
aabccddeddccdda
         |
LIFO: deddccbaa
      |  |

Round 9: Madonna-ing the walrus
aabccddeddccdda
         |
LIFO: ddeddccbaa
      |        |

"""
import time
from typing import Any, Callable

import numpy as np

# # PreClusterity
# ctr_pre: int = 0
# flag_preclusterity: bool = False

# # Clusterity
# idx_cly1: int = 0
# idx_cly2: int = 0
# ctr_cly: int = 0
# flag_clusterity: bool = False

# if flag_preclusterity:

#     if lifo_match1:
#         ctr_pre += 1
#         if ctr_pre == 2:
#             flag_clusterity = True
#             flag_preclusterity = False
#             idx_cly1 = ptr_str - ctr_pre
#             ctr_cly = ctr_pre
#             ctr_pre = 0
#     else:
#         flag_preclusterity = False
#         ctr_pre = 0
# elif lifo_match1:
#     flag_preclusterity = True
#     ctr_pre += 1

# elif flag_clusterity:

#     if lifo_match1:
#         idx_cly2 += 1
#         ctr_cly += 1
#     else:
#         flag_clusterity = False
#         if ctr_cly > current_max:
#             curr_res = (idx_cly1, idx_cly2)
#             current_max = ctr_cly
#         ctr_cly = 0

class Solution:

    # def longestPalindromev1(self, s: str) -> str:

        # LIFO-like list
        # ptr_lifo1: int = -1
        # ptr_lifo2: int = -2
        # flag_isodd: bool = False

        # # Clusteromode
        # idx_clu1: int = 0
        # idx_clu2: int = 0
        # cnt_clu: int = 0
        # clusteromax: int = 0
        # flag_clusteromode: bool = False

        # # Palindromode
        # ptr_pal1: int = 0
        # ptr_pal2: int = 0
        # palindromax: int = 0
        # flag_palindromode: bool = False

        # # Results
        # # hmp_bar: dict[str, bool] = dict()
        # curr_res1: int = 0
        # curr_res2: int = 0

        # for ptr_str, val_str in enumerate(s):

        # if hmp_bar.get(val_str, None):
        #     if flag_clusteromode == False:
        #         flag_clusteromode = True
        #         flag_palindromode = True

        #         clusteromax += 1
        #         palindromax += 1

        #         idx_clu1 = ptr_str

        #         idx_pal1 = ptr_str
        #         ptr_lifo2 -= 1

        #     else:

        #         if flag_clusteromode == True:
        #         flag_clusteromode = True

        #     lifo.append(val_str)
        #     hmp_bar = {val_str: True}
        #     continue
        # else:

        #     curr_lifo1: str = lifo[ptr_lifo1] if 0<=ptr_lifo1<=len(lifo) else ""
        #     curr_lifo2: str = lifo[ptr_lifo2] if 0<=ptr_lifo2<=len(lifo) else ""

        #     print(f"STRING: ptr_str = {ptr_str} | val_str = {val_str}", flush=True)
        #     print(f"LIFO: lifo = {lifo}", flush=True)
        #     print(f"LIFO 1: ptr_lifo1 = {ptr_lifo1} | curr_lifo1 = {curr_lifo1}", flush=True)
        #     print(f"LIFO 2: ptr_lifo2 = {ptr_lifo2} | curr_lifo2 = {curr_lifo2}", flush=True)

        #     lifo_match1: bool = val_str==curr_lifo1 # cmp1
        #     lifo_match2: bool = val_str==curr_lifo2 # cmp2

        #     print(f"MATCH: lifo_match1 = {lifo_match1} | lifo_match2 = {lifo_match2}", flush=True)

        #     if flag_palindromode:

        #         if lifo_match2:
        #             idx_pal1 -= 1
        #             idx_pal2 = ptr_str
        #             ptr_lifo2 -= 2
        #             palindromax += 1
        #             print(f"MATCH2: idx_pal1 = {idx_pal1} | idx_pal2 = {idx_pal2} | ptr_lifo2 = {ptr_lifo2} | palindromax = {palindromax}", flush=True)
        #             if idx_pal1 > 0:
        #                 lifo.append(val_str)
        #                 continue
        #         elif lifo_match1:
        #             print(f"MATCH1: idx_pal1 = {idx_pal1} | idx_pal2 = {idx_pal2} | ptr_lifo2 = {ptr_lifo2} | palindromax = {palindromax}", flush=True)

        #         flag_palindromode = False
        #         ptr_lifo2 = -2
        #         if (this_max := (idx_pal2 - idx_pal1)) > palindromax:
        #             palindromax = this_max
        #             curr_res1 = idx_pal1
        #             curr_res2 = idx_pal2
        #         idx_pal1 = idx_pal2 = ptr_str

        #     elif lifo_match1:
        #         flag_palindromode = True
        #         idx_pal1 = ptr_str
        #         ptr_lifo2 -= 1
        #         palindromax += 1
        #     elif lifo_match2:
        #         flag_palindromode = True
        #         idx_pal1 = ptr_str - 1
        #         ptr_lifo2 -= 2
        #         palindromax += 1

        #     lifo.append(val_str)
        #     # hmp_bar = {val_str: True}

        #     print(f"PAL: flag_palindromode = {flag_palindromode} | idx_pal1 = {idx_pal1} | idx_pal2 = {idx_pal2}", flush=True)
        #     print(f"RES: curr_res1 = {curr_res1} | curr_res2 = {curr_res2} | palindromax = {palindromax}", flush=True)
        #     print("-"*30)

        # if flag_palindromode:
        #     if (this_max := (idx_pal2 - idx_pal1)) > palindromax:
        #         palindromax = this_max
        #         curr_res1 = idx_pal1
        #         curr_res2 = idx_pal2

        # print(f"\nPAL: flag_palindromode = {flag_palindromode} | idx_pal1 = {idx_pal1} | idx_pal2 = {idx_pal2}", flush=True)
        # print(f"RES: curr_res1 = {curr_res1} | curr_res2 = {curr_res2} | palindromax = {palindromax}", flush=True)
        # print("-"*30)

        # out: str = ""
        # out = s[curr_res1-1:curr_res2+1]

        # return out

    def longestPalindrome(self, s: str) -> str:

        # Optimization
        _len: Callable[[str], int] = len
        _range: Callable[[Any], range] = range

        # Encoding input 'bytes' (integers 0-255) and optimization
        sl: bytes = "$".encode('ascii') + s.encode('ascii') + "#".encode('ascii')
        n: int = _len(sl)
        n1: int = n - 1
        n2: int = n1 - 1

        # Array pointers
        ptr_sl1: int = 0
        ptr_sl2: int = 1
        val: int = 0

        # Palindromode | clusterimode
        palindromode: bool = False
        clusterimode: bool = False
        ptr_pldm1: int = 0
        ptr_pldm2: int = 0
        ctr_pldm: int = 1
        ctr_clus: int = 0

        # Result
        ptr_res1: int = 0
        ptr_res2: int = 0
        ctr_out: int = 0

        while True:


            print(f"ptr_sl1 = {ptr_sl1} | ptr_sl2 = {ptr_sl2}")


            if ptr_sl1 == n or ptr_sl2 == n:
                break

            chk1: bool = ptr_sl1 < n1 and sl[ptr_sl1] == sl[ptr_sl2]
            # chk2: bool = ptr_sl2 < n2 and val == sl[ptr_sl2+2]

            print(sl[ptr_sl1], sl[ptr_sl2], sl[ptr_sl1] == sl[ptr_sl2])
            print(f"chk1 = {chk1} | val = {val}")
            print(f"clusterimode = {clusterimode}")

            # Clustering
            if chk1:
                if not clusterimode:
                    clusterimode = True
                ctr_clus += 1

            elif clusterimode:
                clusterimode = False
                if ctr_clus > ctr_out:
                    ctr_out = ctr_clus
                    ptr_res1 = ptr_sl1
                    ptr_res2 = ptr_sl2
                    ctr_clus = 0
                    ptr_sl1 = ptr_sl2

            else:
                ptr_sl1 += 1

            ptr_sl2 = ptr_sl2 + 1

        out: bytes = sl[ptr_res1:ptr_res2]
        print(out)
        out_str: str = out.decode('ascii')

        return out_str

        # while True:

        #     # curr_vec_idx: str = sl[idx_pldm1:idx_pldm2].decode('ascii')
        #     # curr_vec_res: str = sl[res1:res2].decode('ascii')
        #     # print(f"ptr_sl = {ptr_sl} | n1 = {n1} | n = {n}")
        #     # print(f"idx_pldm1 = {idx_pldm1} | idx_pldm2 = {idx_pldm2} | ctr_pldm = {ctr_pldm}")
        #     # print(f"curr_vec_idx = {curr_vec_idx}")
        #     # print(f"res1 = {res1} | res2 = {res2} | ctr_out = {ctr_out}")
        #     # print(f"curr_vec_res = {curr_vec_res}")
        #     if ptr_sl == n:
        #         break

        #     chk1: bool = ptr_sl < n1 and (val := sl[ptr_sl]) == sl[ptr_sl+1]
        #     chk2: bool = ptr_sl < n2 and val == sl[ptr_sl+2]
        #     chkaux: bool = 0 < ptr_auxs < ptr_auxe and val == aux[ptr_auxs]

        #     if chk1 or chk2:
        #         if chk1:
        #             if not palindromode:
        #                 palindromode = True
        #                 idx_pldm1 = ptr_sl
        #                 idx_pldm2 = ptr_sl + 2
        #                 ctr_pldm = 2
        #             else:
        #                 idx_pldm2 += 2
        #                 ctr_pldm += 2
        #             ptr_sl += 2
        #             continue
        #         elif chk2:
        #             if not palindromode:
        #                 palindromode = True
        #                 idx_pldm1 = ptr_sl
        #                 idx_pldm2 = ptr_sl + 3
        #                 ctr_pldm = 3
        #             else:
        #                 idx_pldm2 += 3
        #                 ctr_pldm += 3
        #             ptr_sl += 3
        #             continue
        #     elif chkaux and palindromode:
        #         ptr_sl += 1
        #         idx_pldm1 -= 1
        #         idx_pldm2 += 1
        #         ctr_pldm += 2
        #         ptr_auxs += 1
        #         ptr_auxe -= 1
        #         continue
        #     elif palindromode:
        #         if ctr_pldm > ctr_out:
        #             res1 = idx_pldm1
        #             res2 = idx_pldm2
        #             ctr_out = ctr_pldm
        #         palindromode = False
        #         idx_pldm1 = 0
        #         idx_pldm2 = 0
        #         ctr_pldm = 0

        #     ptr_sl += 1

        #     ptr_auxe += 1
        #     aux[ptr_auxe-1] = val

        # if palindromode:
        #     if ctr_pldm > ctr_out:
        #         res1 = idx_pldm1
        #         res2 = idx_pldm2

        # out: bytes = sl[res1:res2]
        # out_str: str = out.decode('ascii')

        # return out_str


def benchmark(n: int, function: Callable[[str], str], s: str) -> tuple[float, str]:
    times: list[int] = []
    res: str = ""
    for _ in range(n):
        t0: int = time.perf_counter_ns()
        res = function(s)
        t1: int = time.perf_counter_ns()
        times.append(t1 - t0)
    avg: float = np.average(np.array(times))
    return avg, res

if __name__ == "__main__":
    sol = Solution()

    # s = "abba"
    # duration, res = benchmark(1, sol.longestPalindrome, s)
    # print(f"\n### RESULT = {res} | TIME = {duration:.4f} ns", flush=True)

    # s = "cabbad"
    # duration, res = benchmark(1, sol.longestPalindrome, s)
    # print(f"\n### RESULT = {res} | TIME = {duration:.4f} ns", flush=True)

    # s = "cabbadedabb"
    # duration, res = benchmark(1, sol.longestPalindrome, s)
    # print(f"\n### RESULT = {res} | TIME = {duration:.4f} ns", flush=True)

    s = "aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb"
    duration, res = benchmark(1, sol.longestPalindrome, s)
    print(f"\n### RESULT = {res} | TIME = {duration:.4f} ns", flush=True)

    # s = "abcba"
    # duration, res = benchmark(1, sol.longestPalindrome, s)
    # print(f"\n### RESULT = {res} | TIME = {duration:.4f} ns", flush=True)

