def solution(str1, str2):
    answer = 0
    result1 = []
    result2 = []
    answer1 = []
    answer2 = []
    for i in range(len(str1)-1):
        temp1 = str1[i]+str1[i+1]
        if temp1.isalpha():
            result1.append(temp1.upper())
        
    for i in range(len(str2)-1):
        temp2 = str2[i]+str2[i+1]
        if temp2.isalpha():
            result2.append(temp2.upper())
    
    # set_re1 = set(result1)
    # set_re2 = set(result2)
    # mi = len(set_re1 & set_re2)
    # ma = len(set_re1 | set_re2)
    # if ma == 0 and mi == 0:
    #     ans = 1
    # else:
    #     ans = mi / ma
    # answer = ans * 65536
    
    union = len(result1)
    inter = 0
    demo1 = []
    demo2 = []
    
    # 합집합
    for i in result2:
        if i in result1:
            if i not in demo1:
                cnt_re1 = result1.count(i)
                cnt_re2 = result2.count(i)
                if cnt_re1 < cnt_re2:
                    union += cnt_re2 - cnt_re1
                    demo1.append(i)
        else:
            union += 1
    
    # 교집합
    for i in result1:
        for j in result2:
            if i == j:
                if i not in demo2:
                    demo2.append(i)
                    cnt_re1 = result1.count(i)
                    cnt_re2 = result2.count(i)
                    if cnt_re1 < cnt_re2:
                        inter += cnt_re1
                    else:
                        inter += cnt_re2
                    break
                    
    if union == 0 and inter == 0:
        ans = 1
    else:
        ans = inter / union
    answer = ans * 65536
    
    
    return int(answer)