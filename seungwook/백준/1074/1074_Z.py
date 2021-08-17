n, r, c = map(int, input().split())
cnt = 0

while n > 1:
    size = 2**n // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2 # 2사분면을 직접 돌필요 없고 그만큼 cnt를 증가시켜준다.
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2 # 2,1 사분면을 직접 돌필요 없고 그만큼 cnt를 증가시켜준다.
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3 # 3,2,1 사분면을 직접 돌필요 없고 그만큼 cnt를 증가시켜준다.
        r -= size
        c -= size # 사분면 값만큼을 빼줘 2사분면으로 갈수 있도록 한다.
    n -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt+1)
if r == 1 and c == 0:
    print(cnt+2)
if r == 1 and c == 1:
    print(cnt+3)
    
# # 시간초과

# n, r, c = map(int, input().split())

# #graph = [[0] * (2**n) for _ in range(2 ** n)]
# cnt = 0
# def recursive(x,y,size):
#     global cnt
#     if size == 2:
#         if x == r and y == c:
#             print(cnt)
#             return
#         cnt += 1
#         if x == r and y+1 == c:
#             print(cnt)
#             return
#         cnt += 1
#         if x + 1 == r and y == c:
#             print(cnt)
#             return
#         cnt += 1
#         if x + 1 == r and y + 1 == c:
#             print(cnt)
#             return
#         cnt += 1
#     else:
#         size = size//2
#         recursive(x,y,size) # 2사분면
#         recursive(x,y+size, size) # 1사분면
#         recursive(x+size, y, size) # 3사분면
#         recursive(x+size, y+size, size) # 4사분면
# recursive(0, 0, 2**n)

