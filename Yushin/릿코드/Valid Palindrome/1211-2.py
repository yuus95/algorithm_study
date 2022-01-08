class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        for x in s :
            if (x.isalpha() or x.isnumeric()):
                temp +=x
        if (temp[::-1] == temp):
            print(temp)
            return True

        return False

a = Solution()
s = "0P"
print(a.isPalindrome(s))

# print(s.lower())