from typing import *


class Solution:
    def fib(self, n: int) -> int:
        result = [0] * (n + 1)
        if n == 0:
            return 0
        result[0] = 0
        result[1] = 1
        if n < 2:
            return result[n]

        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]


a = Solution()
n = 2
print(a.fib(n))
