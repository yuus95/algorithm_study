from itertools import permutations
import collections
import sys
import copy
INF = sys.maxsize
F = 4

def getPoint(board, curr): # 뽑은 수 쌍에 대한 좌표를 구한다.
    rst = []
    for i in range(F):
        for j in range(F):
            if board[i][j] == curr:
                rst.append((i,j))
    return rst[0], rst[1]

def build(board):
    graph = [[INF] * 16 for _ in range(16)]
    for i in range(F):
        for j in range(F):
            idx = i * F + j
            # 좌
            if j != 0:
                graph[idx][idx - 1] = 1
            # 우
            if j != 3:
                graph[idx][idx + 1] = 1
            # 상
            if i != 0:
                graph[idx][idx - F] = 1
            # 하
            if i != 3:
                graph[idx][idx + F] = 1
            
            # Ctrl 좌
            k = j - 1
            while k >= 0:
                if board[i][k] > 0: # 카드가 있다면 ctrl
                    graph[idx][i*F + k] = 1
                    break
                elif board[i][k] == 0 and k == 0:
                    graph[idx][i*F] = 1
                    break
                k -= 1
            
            # Ctrl 우
            k = j + 1
            while k < F:
                if board[i][k] > 0: # 카드가 있다면 ctrl
                    graph[idx][i*F + k] = 1
                    break
                elif board[i][k] == 0 and k == F - 1:
                    graph[idx][i*F + k] = 1
                    break
                k += 1
            
            # Ctrl 상
            k = i - 1
            while k >= 0:
                if board[k][j] > 0: # 카드가 있다면 ctrl
                    graph[idx][k*F + j] = 1
                    break
                elif board[k][j] == 0 and k == 0:
                    graph[idx][j] = 1
                    break
                k -= 1
            
            # Ctrl 하
            k = i + 1
            while k < F:
                if board[k][j] > 0: # 카드가 있다면 ctrl
                    graph[idx][k*F + j] = 1
                    break
                elif board[k][j] == 0 and k == F - 1:
                    graph[idx][k*F + j] = 1
                    break
                k += 1
    return graph

def bfs(s, e, g):
    i, j = s
    sid = i * F + j
    i, j = e
    eid = i * F + j
    q = collections.deque()
    q.append(sid)
    parents = [-1] * (F*F)
    while len(q) != 0:
        i = q.popleft()
        for j in range(F*F):
            if parents[j] == -1 and g[i][j] != INF:
                parents[j] = i
                q.append(j)
    cnt = 0
    while eid != sid:
        eid = parents[eid]
        cnt += 1
    return cnt

def dist(p1, p2, board, cursor): # cursor부터 p1, p1부터 p2 최단경로 bfs를 통해 계산
    graph = build(board)
    return bfs(cursor, p1, graph) + bfs(p1, p2, graph) + 2 # enter까지 포함

def calc(board, lst, cursor):
    if len(lst) == 0:
        return 0
    b = copy.deepcopy(board) # 원본 board 데이터를 변경하지 않기 위해서 딥카피 후 사용
    l = copy.deepcopy(lst)
    curr = l.pop() # 어떤 숫자 뒤집을 건지 뒤에서 부터 뽑음 (순서는 상관없음)
    p1, p2 = getPoint(board, curr) # 뽑은 수 쌍에 대한 좌표를 구한다.
    d1 = dist(p1, p2, b, cursor) # p2에 위치가 마지막 커서 위치
    d2 = dist(p2, p1, b, cursor) # p1에 위치가 마지막 커서 위치
    i, j = p1 # p1에 x,y
    b[i][j] = 0 # 뒤집은것 0으로 만들어줌
    i, j = p2 # p2에 x,y
    b[i][j] = 0 # 뒤집은것 0으로 만들어줌
    return min(d1 + calc(b, l, p2), d2 + calc(b, l, p1)) # p1에서 p2, p2에서 p1 중에 작은값 선택

def solution(board, r, c):
    s = set()
    for i in range(F):
        for j in range(F):
            s.add(board[i][j])
    s.remove(0)
    answer = INF
    for lst in permutations(s):
        answer = min(answer, calc(board, list(lst), (r,c))) # per원소 lst를 뽑아서 쓸수 있도록 리스트로 변경
    return answer