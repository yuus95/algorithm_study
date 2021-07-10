str = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]



# 가장 짧은 문자열 길이
# 길이는 최대반
# 문자열 전체에 대해 검사
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 문자는 앞에서 하나씩 체크
# 브루트포스 하나씩 다해봐야함
#

#aabbaccc  2abbaccc 2a2baccc 2a2ba3c


def solution(s):
    answer = 0
    n = len(s)

    print(s[0:2])

    # 문자열 길이
    for i in range(1,(n//2)+1):
        #문자열 찾기
        # 문자마다 문자길이만큼 증가시킨 str생성
        for j in range(n):
            if j + i >= n :
                continue
            str = s[j:j+i]
            print(str,end=' ')






    return answer





for s in str:
    print(solution(s))

