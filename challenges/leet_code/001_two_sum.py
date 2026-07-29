class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1: dict[int, int] = {}
        for idx, y in enumerate(nums):
            x_ind: int | None = dict1.get(target-y, None)
            if x_ind is None:
                dict1[y] = idx
                continue
            return [x_ind, idx]