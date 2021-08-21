from collections import defaultdict
from itertools import permutations

def get_distance(r,c, dx, dy):
    if dx != r and dy != c: # 둘다 다른 행렬에 있으면 커서를 두번 움직여야 한다.
        return 2
    elif dx == r and dy == c: # 행과 열이 같다면 안움직여도 된다.
        return 0
    else:
        return 1

def solution(board, r, c):
    answer = []
    card_index = defaultdict(list)
    
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_index[board[i][j]].append((i,j)) # 카드 번호 인덱스에 좌표저장
    
    
    card_numbers = [i for i in range(1, len(card_index) + 1)] # 카드 번호 저장
    
    for orders in permutations(card_numbers, len(card_numbers)): # 카드 번호를 순열로 만들어 모든 경우의수 탐색
        move_cnt = 0
        temp_r, temp_c = r, c
        for num in orders: # 카드 방문 순서
            closest_dst = 1e9
            closest_loc = 0
            dist_list = []
            
            # card_index에 저장한 두 개의 위치에 대한 커서 이동값을 dist_list에 넣어준다.
            for card_dx, card_dy in card_index[num]: # 예를들어 카드번호가 1인 좌표 두개가 들어있다. (0,0), (3,2)  맨 처음 커서에서 각 좌표에 대한 값을 dist_list에 저장한다.
                
                dist_list.append((get_distance(temp_r, temp_c, card_dx, card_dy), card_dx, card_dy))
            
            # 만약 1번카드에서 첫번째 좌표값이 더 가깝다면
            if dist_list[0][0] < dist_list[1][0]:
                move_cnt += dist_list[0][0] # 현재 위치에서 첫번째 좌표까지 더하고
                temp_r, temp_c = dist_list[0][1], dist_list[0][2] # 커서 값을 바꿔주고
                dx, dy = dist_list[1][1], dist_list[1][2]
                move_cnt += get_distance(temp_r,temp_c,dx,dy) # 바뀐 커서 값에서 두번째 좌표까지 이동후 값을 더한다.
                temp_r, temp_c = dx, dy # 커서값 바꾼다.
            
            # 만약 두번쨰 좌표값이 더 가깝다면
            else:
                move_cnt += dist_list[1][0]
                temp_r, temp_c = dist_list[1][1], dist_list[1][2]
                dx,dy = dist_list[0][1], dist_list[0][2]
                move_cnt += get_distance(temp_r, temp_c, dx,dy)
                temp_r, temp_c = dx, dy
                
        answer.append(move_cnt + len(card_index)*2) # 엔터는 카드 갯수*2 이다.
        
    return min(answer) # answer중에 가장 작은값 반환