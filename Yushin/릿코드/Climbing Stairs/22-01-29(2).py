from typing import *

class Solution:
    result= []
    def climbStairs(self, n: int) -> int:
        if len(self.result) == 0 :
            self.result = [0] * (n + 1)
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        if self.result[n] == 0 :
            self.result[n] = Solution.climbStairs(self,n-1)+ Solution.climbStairs(self,n-2)
        return self.result[n]



a = Solution()
n = 4
result = [0] * (n + 1)
print(a.climbStairs(n))
