from itertools import*
_,m=input().split()
print(max(sum(a)for a in combinations(map(int,input().split()),3)if sum(a)<=int(m)))

result = max(sum(a) for a in combinations(map(int, input().split()), 3) if sum(a) <= int(m))
print(result)
