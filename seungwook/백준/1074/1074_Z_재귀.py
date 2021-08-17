# # 시간초과

# n, r, c = map(int, input().split())

# #graph = [[0] * (2**n) for _ in range(2 ** n)]
# cnt = 0
# def recursive(x,y,size):
#     global cnt
#     if size == 2:
#         for i in range(x, x+size):
#             for j in range(y, y+size):
#                 if i == r and j == c:
#                     print(cnt)
#                 cnt += 1
#         return
#     size = size//2
#     recursive(x,y,size) # 2사분면
#     recursive(x,y+size, size) # 1사분면
#     recursive(x+size, y, size) # 3사분면
#     recursive(x+size, y+size, size) # 4사분면
# recursive(0, 0, 2**n)

#####################################################

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

