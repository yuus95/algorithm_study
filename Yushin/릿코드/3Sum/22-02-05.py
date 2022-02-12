from typing import  *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        setNums = set(nums)
        result =[]
        for i in range(len(nums)-2):
            for j in range(i+1 ,len(nums)):
                num = nums[i] + nums[j]
                if -num in nums:
                    for k in range(j+1,len(nums)):
                        if nums[k]== -num:
                            result.append([nums[i],nums[j],nums[k]])
        return result

a =Solution()
nums = [-1,0,1,2,-1,-4]

print(a.threeSum(nums))