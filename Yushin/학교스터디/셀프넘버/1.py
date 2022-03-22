checkbox = [True] * 10001
for i in range(1,10001):
    if i + sum(list(map(int,str(i)))) < 10001:
        checkbox[i + sum(list(map(int, str(i))))] = False

for i in range(1,10001):
    if(checkbox[i]):
        print(i)