def solution(gems):
    set1 = set(gems)
    setLen= len(set1)
    ans = 2147000
    result = []
    for i in range(len(gems)):
        temp= set()
        for j in range(i,len(gems)):
            temp.add(gems[j])
            if len(temp) == setLen:
                if len(result) == 0 :
                    result.append((i,j,j-i))
                elif result[0][2] > j-i:
                    result[0] = (i,j,j-i)
                elif result[0][2] ==j-i:
                    if result[0][0] > i:
                        result[0] = (i,j,j-i)
                break

    # print(result)
    # print(l)
    answer = [result[0][0]+1,result[0][1]+1]

    return answer


gems=[["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],["AA", "AB", "AC", "AA", "AC"],["XYZ", "XYZ", "XYZ"],["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]

for i in range(len(gems)):
    print(solution(gems[i]))