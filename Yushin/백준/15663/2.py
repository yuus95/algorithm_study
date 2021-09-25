import  sys
sys.stdin=open("00.txt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = []

a.sort()
visited = [False] * n  # 방문 여부
count = 0
p = []


def f(depth, n, m):
    if depth == m:
        temp = s.copy()
        p.append(temp)
        print(p)

    for i in range(0, n):
        if not visited[i]:
            visited[i] = True
            s.append(a[i])
            f(depth + 1, n, m)
            s.pop()

            visited[i] = False


f(0, n, m)

for i in p:
    print(i)