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

