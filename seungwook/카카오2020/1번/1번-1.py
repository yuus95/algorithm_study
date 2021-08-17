def solution(s):
    if len(s) <= 2:
        return len(s)
    answerCount = []
    for i in range(1, len(s)//2 + 1):
        answer = []
        result = []
        for j in range(0, len(s), i):
            result.append(s[j:j+i])
        
        count = 1
        for j in range(len(result)):
            if j < len(result)-1 and result[j] == result[j+1]:
                count += 1
            else:
                if count == 1:
                    answer.append(result[j])
                else:
                    answer.append(str(count)+result[j])
                    count = 1
                    
        answerCount.append(len(''.join(answer)))
    return min(answerCount)