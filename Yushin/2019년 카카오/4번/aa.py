#https://velog.io/@qweadzs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8CPython
#생각이안나 다른분 코드 참고

import heapq
def solution(food_times, k):
    answer = 0
    time = 0
    pq = []
    answer_rs = []
    # 1. 우선순위 큐에 (food_times, 음식 번호) 순으로 담는다.
    for i in range(len(food_times)):
        heapq.heappush(pq, [food_times[i], i + 1])

    pre_food = 0
    ok = True

    while ok:
        if not pq:
            return -1
        length = len(pq)
        time += (pq[0][0] - pre_food) * length
        if time > k:
            time -= (pq[0][0] - pre_food) * length
            while pq:
                answer_rs.append(heapq.heappop(pq)[1])
            answer_rs.sort()
            answer = answer_rs[(k - time) % length]
            ok = False
        else:
            pre_food = heapq.heappop(pq)[0]
    return answer