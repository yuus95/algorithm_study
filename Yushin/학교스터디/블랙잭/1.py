import sys
sys.stdin = open("00.txt")

n,m = input().split()
m = int(m)
numberList = list(map(int,input().split()))
numberList.sort()
# numberList.reverse()

len = len(numberList)
result = 0
isOk = False
for x in range(len-2):
    if(isOk):
        break
    for y in range(x+1,len-1):
        if(isOk):
            break
        for z in range(y+1,len):
            sum = numberList[x]+ numberList[y]+numberList[z]
            if(sum <= m and sum > result):
                result = sum
                if(result == m):
                    isOk=True
                    break

print(result)