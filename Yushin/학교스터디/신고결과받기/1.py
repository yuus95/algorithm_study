def solution(id_list, report, k):
    if len(id_list) <=2:
        return [0] * len(id_list)

    result = {}
    resultSet = {}
    userRepostResult = {}
    for i,x in enumerate(id_list) :
        if x not in userRepostResult.keys():
            userRepostResult[x]={}
            result[x] = [i,0]
    for rep in report:
        user,userReport = rep.split(" ")
        if userReport not in userRepostResult[user].keys():
            userRepostResult[user][userReport] = 1
        else:
            userRepostResult[user][userReport]+=1

    for user in userRepostResult:
        resultSet[user] = set()
        for reporter in userRepostResult[user]:
            resultSet[user].add(reporter)
        for x in resultSet[user]:
            result[x][1] +=1

    answer = [0]* len(id_list)

    for resultPerson in result:
        if(result[resultPerson][1] >= k ):
            for id in id_list:
                if resultPerson in resultSet[id]:
                    answer[result[id][0]]+=1
    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list,report,k))
# result = [2,1,1,0]
