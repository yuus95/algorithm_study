from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        result = [0] * (len(nums) + 1)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        result[1] = nums[0]
        result[2] = nums[1]
        result[3] = nums[0] + nums[2]
        maxNum = max(result[2], result[3])

        for i in range(4, len(nums) + 1):
            if result[i - 3] > result[i - 2]:
                result[i] = nums[i - 1] + result[i - 3]
            else:
                result[i] = nums[i - 1] + result[i - 2]
            maxNum = max(maxNum, result[i])

        return maxNum


a = Solution()
nums = [2, 1, 1, 2]
print(a.rob(nums))
