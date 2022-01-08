from typing import *

from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orig = Counter(nums)
        solution_elems = {
            i for i in nums
            if (2 * i == target and orig[i] == 2)
            or (2 * i != target and orig[i] == orig[target - i] == 1)
        }
        return [i for i, v in enumerate(nums) if v in solution_elems]

a = Solution()
nums = [3,2,4]
target = 6
print(a.twoSum(nums,target))