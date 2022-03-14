import sys

sys.stdin = open("00.txt")

text = []
for i in range(9):
    text.append(int(input()))

sum = sum(text)
excludedNumber = []
isOk = False
for i in range(8):
    if(isOk):
        break
    for j in range(i+1,9):
        minusNumber = text[i] + text[j]
        if((sum - minusNumber) == 100):
            excludedNumber.append(i)
            excludedNumber.append(j)
            isOk = True
            break

result = []
for i in range(9):
    if(i in excludedNumber):
        continue
    else:
     result.append(text[i])
result.sort()
print(result)