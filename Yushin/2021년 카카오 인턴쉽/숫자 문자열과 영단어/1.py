def solution(s):
    num = {"zero":0,"one" : 1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    answer  =""
    stack = ""

    for x in s:
        if x.isalpha():
            stack+=x
            if stack in num :
                answer+= str(num[stack])
                stack = ""
        else :
            answer +=x
    return int(answer)



s = ["one4seveneight","23four5six7","2three45sixseven","123"]

for i in range(len(s)):
    print(solution(s[i]))