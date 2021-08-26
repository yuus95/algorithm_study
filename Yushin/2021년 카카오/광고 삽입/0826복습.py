
# 가장 빠른 시작 시각
# answer :"01:30:59" "01:00:00" "00:00:00"
from datetime import datetime


def int_to_str(time):
    h  = time // 3600
    h = '0' + str(h) if h< 10 else str(h)
    time = time % 3600
    m = time //60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h+ ":" + m + ":" + s

def str_to_int(item):
    h,m,s = item.split(":")
    temp = int(h) * 3600 + int(m) *60 + int(s)
    return temp



def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    d = [0] *(play_time*1)

    for i in range(len(logs)):
        x = logs[i].split("-")
        start = str_to_int(x[0])
        end = str_to_int(x[1])
        d[start] += 1
        d[end] -= 1

    for i in range(1,len(d)):
        d[i] +=d[i-1]

    for i in range(1,len(d)):
        d[i] += d[i-1]

    most_view = 0
    max_time = 0

    for i in range(adv_time-1,play_time):
        if i > adv_time:
            if most_view < d[i] - d[i-adv_time]:
                most_view = d[i] - d[i-adv_time]
                max_time = i-adv_time+1
        else:
            if most_view < d[i]:
                most_view = d[i]
                max_time = i-adv_time+1






    return



play_time=["02:03:55","99:59:59","50:00:00"]
adv_time=["00:14:15","25:00:00","50:00:00"]
logs=[["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]


for i in range(len(play_time)):
    print(solution(play_time[i],adv_time[i],logs[i]))