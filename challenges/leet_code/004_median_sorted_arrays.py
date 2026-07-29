"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from __future__ import annotations

import time
from typing import Callable

import numpy as np

def benchmark(n: int, function: Callable, *args):
    times = []
    for _ in range(n):
        t0 = time.perf_counter_ns()
        res = function(*args)
        t1 = time.perf_counter_ns()
        times.append(t1 - t0)
    return np.average(np.array(times)), res

class Solution:

    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays in O(log(min(m, n))) time.

        Parameters
        ----------
        nums1, nums2
            Sorted (non-decreasing) sequences of ints.

        Returns
        -------
        float
            Median of the combined multiset.

        Raises
        ------
        ValueError
            If both inputs are empty.

        Notes
        -----
        This is the standard partition-based binary search solution (same as your C++).
        Recursion (the initial swap) is removed by doing an iterative swap.
        """
        if not nums1 and not nums2:
            raise ValueError("Both arrays are empty.")

        # Ensure nums1 is the smaller array (no recursion)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        NEG_INF = float("-inf")
        POS_INF = float("inf")

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            max_left1 = NEG_INF if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = POS_INF if partition1 == m else nums1[partition1]

            max_left2 = NEG_INF if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = POS_INF if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    left_max = max(max_left1, max_left2)
                    right_min = min(min_right1, min_right2)
                    return (left_max + right_min) / 2.0
                return float(max(max_left1, max_left2))

            if max_left1 > min_right2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        # Should be unreachable if inputs are sorted; keep explicit failure.
        raise ValueError("Inputs must be sorted (non-decreasing).")



    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if not nums1:
            n = len(nums2)
            if n == 0:
                return 0.0
            mid = n >> 1
            if n & 1:
                return float(nums2[mid])
            return (nums2[mid - 1] + nums2[mid]) * 0.5

        if not nums2:
            m = len(nums1)
            mid = m >> 1
            if m & 1:
                return float(nums1[mid])
            return (nums1[mid - 1] + nums1[mid]) * 0.5

        # Ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        a = nums1
        b = nums2
        m = len(a)
        n = len(b)

        half = (m + n + 1) >> 1
        lo = 0
        hi = m

        # Localize builtins (tiny win)
        max_ = max
        min_ = min

        # Use big int sentinels (ints compare faster vs floats here)
        NEG = -10000000
        POS = 10000000

        total_even = ((m + n) & 1) == 0

        while lo <= hi:
            i = (lo + hi) >> 1
            j = half - i

            # Inline boundary checks (avoid float infinities)
            aL = NEG if i == 0 else a[i - 1]
            aR = POS if i == m else a[i]
            bL = NEG if j == 0 else b[j - 1]
            bR = POS if j == n else b[j]

            if aL <= bR and bL <= aR:
                left = aL if aL >= bL else bL
                if not total_even:
                    return float(left)
                right = aR if aR <= bR else bR
                return (left + right) * 0.5

            if aL > bR:
                hi = i - 1
            else:
                lo = i + 1

        return 0.0

    def findMedianSortedArraysOld(self, nums1: list[int], nums2: list[int]) -> float:

        def _sort_1(x: int, y: int, z: int) -> tuple[int, int, int]:
            if x > y:
                if x > z:
                    return y, z, x
                else:
                    return y, x, z
            return x, y, z

        def _sort_2(x: int, y: int, z: int) -> tuple[int, int, int]:
            if z < y:
                if z < x:
                    return z, x, y
                else:
                    return x, z, y
            return x, y, z

        def _finish3() -> float:

            if end_ptr1-sta_ptr1 == 0:
                min_val, med_val, max_val = _sort_1(nums1[sta_ptr1], nums2[sta_ptr2], nums2[end_ptr2])
            else:
                min_val, med_val, max_val = _sort_2(nums1[sta_ptr1], nums1[end_ptr1], nums2[sta_ptr2])
            # med_val = nums1[sta_ptr1+1] if end_ptr2-sta_ptr2 == 0 else nums2[sta_ptr2+1]

            print(f"VALUES: min_val = {min_val}, med_val = {med_val}, max_val = {max_val}")

            if ctr_low == ctr_hi:
                # med_val = max(nums1[sta_ptr1], nums2[sta_ptr2])
                return float(med_val)

            if ctr_low < ctr_hi:
                # max_val = nums1[end_ptr1] if nums1[end_ptr1] >= nums2[end_ptr2] else nums2[end_ptr2]
                return float(med_val + max_val) / 2.0
            # min_val = nums1[sta_ptr1] if nums1[sta_ptr1] <= nums2[sta_ptr2] else nums2[sta_ptr2]
            return float(min_val + med_val) / 2.0

        # Optimization settings
        # median_index = (local_len(sorted_list) - 1) >> 1
        local_len: int = len
        finish3: float = _finish3

        # Parameters
        tot_nums1_1: int = (tot_nums1 := local_len(nums1)) - 1
        tot_nums2_1: int = (tot_nums2 := local_len(nums2)) - 1
        tot_thresh: int = (tot_nums := tot_nums1 + tot_nums2) - 3
        tot_thresh1: int = tot_thresh - 1
        is_even: bool = tot_nums%2==0

        # Counters
        ctr_low: int = 0
        ctr_hi: int = 0
        ctr_tot: int = 0

        # Pointers
        sta_ptr1: int = 0
        med_ptr1: int = (tot_nums1 - 1) >> 1
        end_ptr1: int = tot_nums1-1
        sta_ptr2: int = 0
        med_ptr2: int = (tot_nums2 - 1) >> 1
        end_ptr2: int = tot_nums2-1

        # print(f"INPUT: nums1 = {nums1} | nums2 = {nums2}")
        # print(f"TOTALS: tot_nums1 = {tot_nums1} | tot_nums2 = {tot_nums2}")
        # print(f"VEC1: sta_ptr1 = {sta_ptr1} | med_ptr1 = {med_ptr1} | end_ptr1 = {end_ptr1}")
        # print(f"VEC2: sta_ptr2 = {sta_ptr2} | med_ptr2 = {med_ptr2} | end_ptr2 = {end_ptr2}")
        # print("-"*20)

        # Extreme cases
        if tot_nums1 == 0 and tot_nums2 == 0:
            return 0.0
        elif tot_nums1 == 1 and tot_nums2 == 1:
            return float(nums1[0] + nums2[0])/2.0
        elif tot_nums1 == 1 and tot_nums2 == 0:
            return float(nums1[0])
        elif tot_nums1 == 0 and tot_nums2 == 1:
            return float(nums2[0])
        elif tot_nums1 == 0:
            return float(nums2[med_ptr2]) if not is_even else float(nums2[med_ptr2] + nums2[med_ptr2+1])/2.0
        elif tot_nums2 == 0:
            return float(nums1[med_ptr1]) if not is_even else float(nums1[med_ptr1] + nums1[med_ptr1+1])/2.0

        counter = 1

        while True:

            print(f"Interation {counter}")
            print(f"VEC1: sta_ptr1 = {sta_ptr1} | med_ptr1 = {med_ptr1} | end_ptr1 = {end_ptr1}")
            print(f"VEC2: sta_ptr2 = {sta_ptr2} | med_ptr2 = {med_ptr2} | end_ptr2 = {end_ptr2}")
            print("-"*20)

            # Postlude
            if ctr_tot == tot_thresh:
                return finish3()
            elif ctr_tot >= tot_thresh:
                return "ERROR"

            # Main Check
            if ctr_tot == tot_thresh1 and nums1[med_ptr1] == nums2[med_ptr2]:
                if ctr_low < ctr_hi:
                    val_1 = nums1[sta_ptr1]
                    val_2 = nums2[sta_ptr2]
                    if val_1 <= val_2:
                        ctr_low += 1
                        sta_ptr2 = sta_ptr2 + 1
                    else:
                        ctr_low += 1
                        sta_ptr1 = med_ptr1 + 1
                else:
                    val_1 = nums1[end_ptr1]
                    val_2 = nums2[end_ptr2]
                    if val_1 <= val_2:
                        ctr_hi -= 1
                        end_ptr2 = med_ptr2 - 1
                    else:
                        ctr_hi -= 1
                        end_ptr1 = med_ptr1 - 1
            elif nums1[med_ptr1] <= nums2[med_ptr2]:
                ctr_low += med_ptr1 - sta_ptr1 if med_ptr1 > sta_ptr1 else 0
                ctr_hi += end_ptr2 - med_ptr2 if end_ptr2 > med_ptr2 else 0
                sta_ptr1 = med_ptr1 if med_ptr1 > 0 else 0
                end_ptr2 = med_ptr2 if med_ptr2 < tot_nums2_1 else tot_nums2_1
            else:
                ctr_low += med_ptr2 - sta_ptr2 if med_ptr2 > sta_ptr2 else 0
                ctr_hi += end_ptr1 - med_ptr1 if end_ptr1 > med_ptr1 else 0
                end_ptr1 = med_ptr1 if med_ptr1 < tot_nums1_1 else tot_nums1_1
                sta_ptr2 = med_ptr2 if med_ptr2 > 0 else 0

            ctr_tot = ctr_low + ctr_hi
            med_ptr1 = int((end_ptr1 + sta_ptr1) / 2)
            med_ptr2 = int((end_ptr2 + sta_ptr2) / 2)

            print(f"VEC1: sta_ptr1 = {sta_ptr1} | med_ptr1 = {med_ptr1} | end_ptr1 = {end_ptr1}")
            print(f"VEC2: sta_ptr2 = {sta_ptr2} | med_ptr2 = {med_ptr2} | end_ptr2 = {end_ptr2}")
            print(f"COUNT: ctr_low = {ctr_low} | ctr_hi = {ctr_hi}")
            print("="*30)
            if counter == 30:
                break

            counter += 1
            # med_idx1 = (local_len(nums1) - 1) >> 1
            # updated_total += (total_a := total_a + amount) + (total_b := total_b + other_amount)

if __name__ == "__main__":
    s = Solution()

    # vec1 = []
    # vec2 = []
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = [10]
    # vec2 = []
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = []
    # vec2 = [10]
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = []
    # vec2 = [10,20]
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = [10,20]
    # vec2 = []
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = [10]
    # vec2 = [20]
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = [10]
    # vec2 = [20,30]
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    # vec1 = [10,30,50,70,90]
    # vec2 = [5,20,40,60,80]
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

    vec1 = [10]*1000 + [30]*1000 + [50]*1000 + [70]*1000 + [90]*1000
    vec2 = [5]*1000 + [20]*1000 + [40]*1000 + [60]*1000 + [80]*1000
    fmed = np.median(vec1 + vec2)
    duration, res = benchmark(1000, s.findMedianSortedArrays, vec1, vec2)
    print(f"### RESULT = {res} | TIME = {duration:.4f} ns")
    print(fmed)

    # vec1 = [2, 2, 4, 4]
    # vec2 = [2, 2, 2, 4, 4]
    # duration, res = benchmark(1, s.findMedianSortedArrays, vec1, vec2)
    # print(f"### RESULT = {res} | TIME = {duration:.4f} ns")

