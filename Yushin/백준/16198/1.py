import  sys
sys.stdin=open("00.txt")

n = int(input())

a = list(map(int,input().split()))
answer = 0
check = [False] * n
def dfs(l,sum,temp,lenx):
    global  answer

    if l == 2 :
        if answer < sum :
            answer = sum


    else :
        for i in range(1,lenx-1,1):
            # print(temp)
            num = temp[i-1] * temp[i+1]
            test = temp[:i] + temp[i+1:]
            dfs(l-1,sum+num,test,len(test))


dfs(n,0,a,n)
print(answer)
