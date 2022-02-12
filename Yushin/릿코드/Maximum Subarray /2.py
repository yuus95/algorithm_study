from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        s = max(result, 0)
        for n in nums[1:]:
            s += n
            result = max(result, s)
            s = max(s, 0)
        return result


a = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(a.maxSubArray(nums))
