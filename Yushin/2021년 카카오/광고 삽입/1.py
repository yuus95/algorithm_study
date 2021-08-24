
# 가장 빠른 시작 시각
# answer :"01:30:59" "01:00:00" "00:00:00"
from datetime import datetime
def time_to_sec(t):
   h, m, s= map(int, t.split(':'))
   return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    n = len(logs)
    adv = time_to_sec(adv_time)
    ans = [0,0]
    for i in range(n-1):
        x = logs[i].split("-")
        st = time_to_sec(x[0])
        et = time_to_sec(x[1])
        adv_et = st+adv
        temp = et-st
        for j in range(i+1,n):
            y = logs[j].split("-")
            j_st = time_to_sec(y[0])
            j_ed = time_to_sec(y[1])

            if j_st > adv_et or j_ed < st:
                continue
            temp += (adv_et - j_st)

        if ans[1] < temp:
            ans[1] = temp
            ans[0] = i
    print(ans)


    answer = ''
    return logs[ans[0]].split("-")[0]



play_time=["02:03:55","99:59:59","50:00:00"]
adv_time=["00:14:15","25:00:00","50:00:00"]
logs=[["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]


for i in range(len(play_time)):
    print(solution(play_time[i],adv_time[i],logs[i]))