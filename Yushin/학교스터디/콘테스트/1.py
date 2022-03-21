import sys

sys.stdin = open("00.txt")


num1 = []
num2 = []
for i in range(10):
    num1.append(int(input()))

for i in range(10):
     num2.append(int(input()))

num1.sort()
num2.sort()

print(num1[9]+num1[8]+num1[7],num2[9]+num2[8]+num2[7])