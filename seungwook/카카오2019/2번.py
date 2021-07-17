def solution(N, stages):
    answer = []
    people=len(stages)
    print(people)
    result = []
    for i in range(1, N+1):
        count = 0        
        for j in range(len(stages)):
            if i == stages[j]:
                count += 1
                
        if people == 0:
            result.append([i, 0])
            continue
            
        result.append([i, count / people])
        people -= count
    
    result.sort(key = lambda x : x[1], reverse=True)
    
    for x,y in result:
        answer.append(x)
    return answer