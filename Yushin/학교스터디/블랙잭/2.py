import sys
sys.stdin = open("00.txt")

n,m = input().split()
m = int(m)
numberList = list(map(int,input().split()))

def buildSum(numberList,m):
    result = 0
    size = len(numberList)
    for x in range(size-2):
        for y in range(x+1,size-1):
            for z in range(y+1,size):
                sum = numberList[x]+ numberList[y]+numberList[z]
                if(sum <= m and sum > result):
                    result = sum
                    if(result == m):
                        return result
    return result


build_sum = buildSum(numberList, m)
print(build_sum)