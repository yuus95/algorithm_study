class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = list(filter(str.isalnum, s.lower()))
        return forward == forward[::-1]
