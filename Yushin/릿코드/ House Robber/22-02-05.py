from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        sumNum = [0] * len(nums)
        sumNum[0] = nums[0]
        sumNum[1] = nums[1]
        sumNum[2] = nums[0] + nums[2]
        result = max(sumNum[1],sumNum[2])
        for i in range(3,len(nums)):
            if sumNum[i-3] + nums[i] > sumNum[i-2] + nums[i]:
                sumNum[i] =  sumNum[i-3] + nums[i]
            else :
                sumNum[i] = sumNum[i-2] + nums[i]
            result = max(result,sumNum[i])
        return result
a = Solution()
nums = [2, 1, 1, 2]
print(a.rob(nums))
