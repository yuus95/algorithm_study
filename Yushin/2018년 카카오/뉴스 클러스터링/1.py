def solution(str1, str2):
    answer = 0


    str1_box = []
    str2_box = []


    # 문자열에서 모든 2글자의 조합을 찾아냄
    for i in range(1,len(str1)):
        x1 = str1[i-1]
        if not x1.isalpha():
            continue

        x2 = str1[i]

        if not x2.isalpha():
            continue
        x1 = x1.lower()
        x2 = x2.lower()

        str1_box.append(x1+x2)

    for i in range(1,len(str2)):
        x1 = str2[i-1]
        if not x1.isalpha():
            continue

        x2 = str2[i]

        if not x2.isalpha():
            continue
        x1 = x1.lower()
        x2 = x2.lower()

        str2_box.append(x1+x2)


    print(str1_box)
    print(str2_box)

    # check박스를 만들고 난뒤 중복을 피해 교집합을 만든다.
    check_box = [False] * len(str2_box)
    cnt = 0
    for i in range(len(str1_box)):
        temp = str1_box[i]
        for j in range(len(str2_box)):
            if temp == str2_box[j]:
                if not check_box[j]:
                    check_box[j] = True
                    cnt+=1
                    break
    sum_box = len(str1_box)+len(str2_box)-cnt

    if cnt == 0 and sum_box == 0 :
        return 65536

    answer = cnt/sum_box  * 65536


    return int(answer)

str1= ["FRANCE","handshake","aa1+aa2","E=M*C^2"]
str2= ["french","shake hands","	AAAA12","e=m*c^2"]


for i in range(4):
    print(solution(str1[i],str2[i]))