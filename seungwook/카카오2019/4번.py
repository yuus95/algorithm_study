# 시간초과 O(N) 풀이로는 food_times에 길이가 1억이므로 시간초과가 난다.
# O(logn) 풀이 찾아야함
def solution(food_times, k):
    answer = 0
    cnt = 0
    while True:
        if food_times[cnt%len(food_times)] != 0:
            food_times[cnt%len(food_times)] -= 1
        else:
            cnt += 1
            continue
        k -= 1
        cnt += 1
        
        if k == 0:
            break
            
    while True:
        if food_times[cnt%len(food_times)] == 0:
            cnt += 1
        else:
            break
            
    return cnt%len(food_times) + 1