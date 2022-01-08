from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(nums)):
            hashmap[nums[i]]= i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!= i :
                return [i,hashmap[complement]]


a = Solution()
nums = [3,2,4]
target = 6
print(a.twoSum(nums,target))