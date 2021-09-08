def solution(n, k, cmds):
    nodes = {0 : [n-1, 1]}
    for i in range(1,n):
        if i == n-1:
            nodes[i] = [i-1, 0]
        else:
            nodes[i] = [i-1, i+1] # 이전값(pre), 다음값(next)
    
    stack = []
    for cmd in cmds:
        if len(cmd) > 1:
            c, x = cmd.split()
            cnt = 0
            # "D X"
            if c == 'D': # C 에서 값을 제거해주기 때문에 값을 더해주는게 아니라 연결리스트를 타고 움직여야한다.
                while cnt < int(x):
                    k = nodes[k][1]
                    cnt += 1
            # "U X"
            else:
                while cnt < int(x):
                    k = nodes[k][0]
                    cnt += 1
        else:
            # "C"
            if cmd == 'C':
                nodes[nodes[k][0]][1] = nodes[k][1] # 현재값을 삭제하니까 이전값에 next노드가 현재값에 next를 가리키도록 해준다.
                nodes[nodes[k][1]][0] = nodes[k][0] # 현재값을 삭제하니까 다음값에 pre노드가 현재값에 pre를 가리키도록 해준다.
                stack.append([k, nodes[k]])
                tmp = nodes[k]
                del nodes[k]

                if tmp[1] == 0: # next가 없을경우는 맨 마지막 값인 경우
                    k = tmp[0] # 그럴 경우에는 pre노드 값으로 커서를 바꾼다.
                else:
                    k = tmp[1]
            else:
                curr_node, val = stack.pop()
                prev_node, next_node = val
                nodes[curr_node] = [prev_node, next_node]
                nodes[prev_node][1] = curr_node
                nodes[next_node][0] = curr_node

    result = ''
    for i in range(n):
        if nodes.get(i) is None:
            result += 'X'
        else:
            result += 'O'
    return result
