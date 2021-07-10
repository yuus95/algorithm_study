def solution(s):
    answer = 99999999
    for i in range(1, len(s)//2 + 1):
        ret = ""
        count = 1
        prev = s[:i]
        for j in range(i, len(s)+i, i): # 맨마지막값 len(s)+i 가 아무리 크더라도 s[:len(s)+1]는 len(s)+1가 없는 
                                        # index더라도 index에러가 안난다.
                                        # +i씩 증가하므로 맨마지막 값을 비교못하는 순간을 제외하기 위해서
                                        # len(s) + i를 해준다.
            if prev == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    ret = ret + str(count) + prev
                else:
                    ret = ret + prev
                prev = s[j:j+i]
                count = 1
        answer = min(answer, len(ret))
    return answer