from itertools import combinations
from collections import deque
def solution(relation):
    answer = 0
    n = len(relation)
    m = len(relation[0])
    
    coms = []
    for i in range(1, m+1):
        coms.extend(list(combinations(range(m), i))) # 모든 자리수에 조합을 com에 넣는다.
        # append와 extend에 차이점은 extend는 확장에 개념으로 리스트에 리스트를 추가하더라도 한개의 리스트가 된다.
        # ex) a = [1,2,3]
        # a.extend([4]) => a = [1,2,3,4]
        # 반면 append는 요소를 넣는 개념으로 a = [1,2,3,[4]] 가 된다.
    
    # 유일성 만족하는 키 찾기
    keys = deque()
    for com in coms:
        
        temp = ['' for _ in range(n)]
        for i in com: 
            for idx, j in enumerate(relation): # enumerate는 range를 안돌려서 index가 없을때 index를 만들어서 사용할수있다.
                temp[idx] += j[i]
                
        if len(set(temp)) == n:
            keys.append(com)
    
    # 최소성 만족하는 키 찾기
    while keys:
        temp = keys.popleft() # keys에 가장 먼저 들어온 값이 가장 최소성을 만족하므로 popleft를 해준다.
        answer += 1
        new = deque()
        for key in keys:
            print(key)
            if len(set(key) - set(temp)) != len(key) - len(temp): # set 차집합 연산을 이용해 값은게 있을경우에는 길이 빼주는 값과 동일하게 나온다.
                # 두 길이가 다르다는 것은 공통된 부분이 없다는 뜻이다.
                new.append(key) # new에는 최소성을 만족하는 키를 넣어준다.
        keys = new # 최소성을 다시한번 검증하기 위해 keys에 넣어주고 while문을 돈다.
        
    return answer