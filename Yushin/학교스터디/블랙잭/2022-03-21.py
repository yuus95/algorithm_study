import sys

sys.stdin = open("00.txt")


def solution(numbers):
    result = 0
    for x1 in range(0, n - 2):
        for x2 in range(x1 + 1, n - 1):
            for x3 in range(x1+2 + 1, n):
                tempSum = numbers[x1] + numbers[x2] + numbers[x3]
                if result <= tempSum <= m:
                    result = tempSum
                    if result == m:
                        return result
    return result


n, m = map(int, input().split(" "))
inputList = list(map(int, input().split(" ")))

print(solution(inputList))
