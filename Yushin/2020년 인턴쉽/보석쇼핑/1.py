def solution(gems):
    set1 = set(gems)
    ans = 2147000
    result = []
    for i in range(len(gems)):
        temp= set()
        for j in range(i,len(gems)):
            temp.add(gems[j])
            if len(temp) == len(set1):
                result.append([i,j,j-i])
                break

    # print(result)
    l = sorted(result, key=lambda x: (x[2], x[0]))
    # print(l)
    answer = []
    answer.append(l[0][0]+1)
    answer.append(l[0][1]+1)
    return answer


gems=[["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],["AA", "AB", "AC", "AA", "AC"],["XYZ", "XYZ", "XYZ"],["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]

for i in range(len(gems)):
    print(solution(gems[i]))