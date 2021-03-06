from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        result = nums[0]
        if len(nums) >= 1:
            for i in range(1, len(nums)):
                if nums[i] > nums[i] + prev:
                    prev = nums[i]
                else:
                    prev = nums[i] + prev
                result = max(result, prev)
        return result


a = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(a.maxSubArray(nums))
