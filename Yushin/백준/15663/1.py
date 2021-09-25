import  sys
sys.stdin=open("00.txt")

n, m = map(int,input().split())

a = list(map(int,input().split()))
a.sort()

test = []

check = [False] * n
def dfs(l,x,k):
    if l == m:
        if m == len(x):
            test.append(x)

    for i in range(k,n):
        if check[i] == False:
            check[i] =True
            dfs(l+1,x+[a[i]],k+1)
            check[i]=False

dfs(0,[],0)
print(test)