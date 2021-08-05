
new_id = ["...!@BaT#*..y.abcdefghijklm","z-+.^.","=.=",	"123_.def","abcdefghijklmn.p"]

def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    #2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-','.','_']:
            answer+=c

    #3단계
    while '..' in answer:
        answer=answer.replace('..','.')

    # 4단계
    if answer[-1] == '.':
        answer=answer[:-1]
    if len(answer) > 0 and  answer[0] == '.':
        answer = answer[1:]


    if len(answer) < 1 :
        answer = "a"


    #6단계
    if len(answer) > 15:
        answer= answer[:15]

    if answer[-1] == '.':
        answer= answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]


    return answer



for i in range(len(new_id)):
    print(solution(new_id[i]))

