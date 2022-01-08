from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        s = s.lower()
        for str in s:
            if str.isalpha() or str.isnumeric():
                temp+=str
        if len(s) == 1:
            return True
        for i in range(len(temp)//2):
            if temp[i] != temp[len(temp)-1-i]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))