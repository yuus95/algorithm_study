# 왼쪽 숫자는 직원번호
#  오른쪽 숫자는 해당 직원의 하루평균 매출액을 나타냅니다.
# 모든 팀은 최소 1명 이상
# 직원들의 하루평균 매출액 값을 담은 배열 sale
# 소 한 명 이상 워크숍에 참석하면서, 참석하는 직원들의 하루평균 매출액의 합을 최소로 하려고 합니다.

answer = 0

def dfs(idx,num,d,team,check,money):
    global  answer
    if idx == len(d):
        if answer > num :
            answer = num
        return

    for x in check:
        if x in team[d[idx]]:
            dfs(idx+1,num,d,team,check,money)


    for i in range(len(team[d[idx]])):
        dfs(idx+1,num+money[team[d[idx]][i]],d,team,check+[team[d[idx]][i]],money)



def solution(sales, links):
    global answer
    global sum_m
    answer=214700000

    money = [0] * (len(sales)+1)
    team = {}
    # 직원 매출액
    for i in range(len(sales)):
        money[i+1] = sales[i]

    sum_m = sum(money)
    # x:팀장
    # y:팀원
    for x,y in links:
        if x in team.keys():
            team[x].append(y)
        else:
            team[x]=[y]

    # 키번호
    d = list(team.keys())

    # 팀장 번호, num
    dfs(0,0,d,team,[],money)


    return answer


sales = [[14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[5, 6, 5, 3, 4],[5, 6, 5, 1, 4],[10, 10, 1, 1]]
links = [[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],	[[2,3], [1,4], [2,5], [1,2]],[[2,3], [1,4], [2,5], [1,2]],[[3,2], [4,3], [1,4]]]


for i in range(len(sales)):
    print(solution(sales[i],links[i]))
