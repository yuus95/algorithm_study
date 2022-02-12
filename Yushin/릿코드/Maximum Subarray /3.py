from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1],nums[0]+nums[1])
        for i in range(1,len(nums)):
            if nums[i] <= nums[i] + nums[i-1]:
                nums[i] =  nums[i] + nums[i-1]
            result = max(result,nums[i])
        return result

a = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(a.maxSubArray(nums))
