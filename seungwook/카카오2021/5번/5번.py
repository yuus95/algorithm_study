# 안됨 다시풀어보기
import sys

def solution(play_time, adv_time, logs):
    answer = ''
    result = []
    demo = []
    
    for i in logs:
        i = i.split('-')
        for j in i:
            j = j.split(':')
            result.append(j)
        
    for i in result:
        answer = 0
        answer += int(i[0]) * 60 * 60
        answer += int(i[1]) * 60
        answer += int(i[2])
        demo.append(answer)
    #print(demo)
    adv = adv_time.split(':')
    target = int(adv[0]) * 60 * 60 + int(adv[1]) * 60 + int(adv[2])
    #print(target)
    final = []
    for i in range(0, len(demo)-1, 2):
        count = 0
        point = demo[i] + target
        for j in range(0, len(demo)-1, 2):
            if demo[j] <= point <= demo[j+1]:
                count += 1
        final.append(count)
    #print(final)
    minn = sys.maxsize
    idx = final.index(max(final))
    cnt = final.count(max(final))
    if max(final) == 0:
        return "00:00:00"
    for id, i in enumerate(final):
        if i == max(final):
            minn = min(minn, demo[id*2])
    
    idx = demo.index(minn) // 2
    #print(idx)    
    return logs[idx].split("-")[0]