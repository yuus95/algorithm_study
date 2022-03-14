import sys
sys.stdin = open("00.txt")

n,m = input().split()
m = int(m)
numberList = list(map(int,input().split()))
result = []
maxNum = 0

def recursiveFun(sum,l,numberList,m,cnt):
    global maxNum;
    if sum > m:
        return

    if cnt < 0 :
        return

    if len(numberList) == l:
        if sum <= m and cnt == 0:
            if maxNum < sum:
                maxNum = sum
            return
        return

    recursiveFun(sum+numberList[l],l+1,numberList,m,cnt-1)
    recursiveFun(sum,l+1,numberList,m,cnt)
    return maxNum

recursiveFun(0,0,numberList,m,3)
result.sort()
result = result[::-1]
print(maxNum)
