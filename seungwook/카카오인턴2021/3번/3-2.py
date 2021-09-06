from bisect import bisect_left, bisect_right
def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    graph = [i for i in range(n)]
    temp = [i for i in range(n)]
    queue = []
    end = len(graph)-1
    for i in cmd:
        i = i.split()
        if i[0] == 'U':
            k -= int(i[1])
            while graph[k] == -1:
                k -= 1
        elif i[0] == 'D':
            k += int(i[1])
            while graph[k] == -1:
                k += 1
        elif i[0] == 'C':
            queue.append(graph[k])
            graph[k] = -1
            if k == len(graph)-1:
                k -= 1
            else:
                k += 1
            
        elif i[0] == 'Z':
            re = queue.pop() # re는 유일한 값 (0,1,2 ...)
            graph[re] = re
            # if k >= re: # bi(들어갈 위치)가 인덱스 보다 작을 경우 인덱스 밀려야함 선택된 값이 안바뀌기 위해
            #     k += 1 
        
    set_graph = set(graph)
    set_temp = set(temp)
    demo = set_temp - set_graph
    for i in demo:
        answer[i] = 'X'
    
    return ''.join(answer)