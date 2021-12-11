from typing import *

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        temp_dict = dict()
        paragraph = paragraph.lower()
        paragraph = list(paragraph)
        print(paragraph)
        for i in range(len(paragraph)):
            temp = ""
            for x in paragraph[i]:
                if x.isalpha():
                    temp+= x
                paragraph[i]=temp
        for x in paragraph:
            if x in banned:
                continue
            if x in temp_dict.keys():
                temp_dict[x] +=1
            else:
                temp_dict[x] = 1
        maxNum = 0
        answer = ""
        for i in temp_dict.keys():
           if maxNum < temp_dict[i]:
               maxNum = temp_dict[i]
               answer = i
        return answer

a = Solution()
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["hit"]
print(a.mostCommonWord(paragraph,banned))
