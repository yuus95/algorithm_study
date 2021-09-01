
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
    d = [0] *(play_time+1)

    # 시작점과 끝점 +1 , -1 삽입
    for i in range(len(logs)):
        x = logs[i].split("-")
        start = str_to_int(x[0])
        end = str_to_int(x[1])
        d[start] += 1
        d[end] -= 1

    # 구간구하기
    for i in range(1,len(logs)):
        d[i]+= d[i-1]

    currSum = sum(d[:adv_time])
    maxSum = currSum
    maxIdx= 0

    for i in range(adv_time,play_time):
        currSum = currSum + d[i] - d[i-adv_time]
        if currSum > maxSum :
            maxSum = currSum
            maxIdx = i-adv_time+1
            # 여기서 1초를 더해준 이유는 timeline[end] - timeline[start]가
            # start+1초 부터 end초사이의 누적 시간이기 때문에

    answer = '%02d:%02d:%02d' %(maxIdx/3600,maxIdx/60%60,maxIdx%60)




    return answer



play_time=["02:03:55","99:59:59","50:00:00"]
adv_time=["00:14:15","25:00:00","50:00:00"]
logs=[["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]


for i in range(len(play_time)):
    print(solution(play_time[i],adv_time[i],logs[i]))