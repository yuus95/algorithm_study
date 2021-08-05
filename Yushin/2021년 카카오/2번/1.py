from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    # b = order.sort()
    # 문자열에서는 문자열.sort()불가능
    # 콤비네이션 자체는 주소를 반환하지만 배열에 더하면 데이터가 된다.
    # 코스배열에서  코스 음식 갯수 가져와서 조합만들기
    for co in course:

        temp = []
        for order in orders:
            order = ''.join(sorted(order))
            # combi = list(combinations(order,co))
            combi = combinations(order,co)
            temp += combi

            # temp += combination(sorted(order),co)
        counter = Counter(temp)
        # most_common() 데이터개수가 많은순으로 정렬
        # counter = Counter(temp).most_common()


        # answer += [k for k,v in most_ordered if v > 1 and v == most_ordered[0][1]]
        if len(counter) > 0 and  max(counter.values()) >= 2:
            append_row = [x for x in counter if max(counter.values()) == counter[x]]
            for x in append_row:
                test1 = ''.join(x)
                answer.append(test1)

    # answer = [''.join(v) for v in sorted(result)]
    answer=sorted(answer)
    return answer



orders =[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],["XYZ", "XWY", "WXA"]]
course = [[2,3,4],[2,3,5],[2,3,4]]



for i in range(3):
    print(solution(orders[i],course[i]))
