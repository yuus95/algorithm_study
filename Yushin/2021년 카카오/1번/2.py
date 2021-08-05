# 정규식방법 다른사람풀이 참고
new_id = ["...!@BaT#*..y.abcdefghijklm","z-+.^.","=.=",	"123_.def","abcdefghijklmn.p"]


import re


# ^ : 맨처음을 의미함
# $ : 맨뒤를 의미함
# | : or 의미
# group : 반복되는 문자열을 찾을 떄 사용



def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st



for i in range(len(new_id)):
    print(solution(new_id[i]))

