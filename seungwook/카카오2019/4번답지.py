def solution(food_times, k):
    foods = []
    n = len(food_times) # 총 음식의 갯수
    for i in range(n):
        foods.append((food_times[i], i+1)) # 음식의 시간과 음식번호를 저장한다.
        
    foods.sort() # 음식을 한번에 빼기 위해서 오름차순 정렬을 시켜준다.
    
    pretime = 0 # 전 음식의 시간(높이)
    for i, food in enumerate(foods):
        diff = food[0] - pretime # 현재 음식의 시간 - 전 음식의 시간
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n # k보다 spend가 크면 한번에 못빼므로 나머지 연산으로 어느 위치인지 구한다.
                sublist = sorted(foods[i:], key = lambda x : x[1]) # 현재 남아있는 음식의 인덱스는 i이후 이고, 다시 음식의 번호 기준으로 정렬하기 위해 x[1] 기준으로 정렬한다.
                return sublist[k][1]
        n -= 1
    return -1
        