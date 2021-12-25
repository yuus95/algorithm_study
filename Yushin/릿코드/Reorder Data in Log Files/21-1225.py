from typing import *


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        strList = []
        numList = []

        for x in logs:
            xList = list(x.split())
            if xList[1].isnumeric():
                numList.append(x)
            else:
                strList.append(x)
        strList = sorted(strList, key=lambda x: (x.split()[1:], x.split()[0]))
        return logs


a = Solution()

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(a.reorderLogFiles(logs))
