from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1
        result = [0] * (n+1)
        result[0] = 1
        result[1] = 1
        result[2] = 2
        for i in range(2,n+1):
            result[i] = result[i-1] + result[i-2]
        print(result)
        return result[n]



a = Solution()
n = 4
print(a.climbStairs(n))
