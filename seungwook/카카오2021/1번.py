def solution(new_id):
    answer = 0
    # 1
    new_id = new_id.lower()
    new_id_list = list(new_id)
    #print(ord('.')) # a~z : 97 ~ 122
                    # 0~9 : 48 ~ 57, - : 45, _ : 95, . : 46
    print(new_id_list)
    delete = []
    # 2
    for i in range(len(new_id_list)):
        if 97 <= ord(new_id_list[i]) <= 122 or 48 <= ord(new_id_list[i]) <= 57 or 45 <= ord(new_id_list[i]) <= 46 or ord(new_id_list[i]) == 95:
            continue
        else:
            delete.append(new_id_list[i])
    
    for i in delete:
        new_id_list.remove(i)
    print(new_id_list) 
#     # 3
    comma = []
    leng = len(new_id_list)
    for i in range(leng-1):
        count = 1
        if new_id_list[i] == '.':
            if new_id_list[i+1] == '.':
                comma.append(i)
    print(comma)
    cnt = 0
    for i in comma:
        new_id_list.pop(i-cnt)
        cnt += 1
    
            # for j in range(i+1, len(new_id_list)):
            #     if new_id_list[j] == '.':
            #         count += 1
            #     else:
            #         break
            # if count >= 2:
            #     for i in range(count-1):
            #         new_id_list.remove('.')
                
    
    print(new_id_list)
 # 4
    if new_id_list[0] == '.':
        new_id_list.pop(0)
    if len(new_id_list) == 0:
        new_id_list.append('a')
    if new_id_list[-1] == '.':
        new_id_list.pop()
#     # 5    
    if len(new_id_list) == 0:
        new_id_list.append('a')
        
#     # 6
    if len(new_id_list) >= 16:
        new_id_list = new_id_list[0:15]
    if new_id_list[-1] == '.':
        new_id_list.pop(-1)
        
#     # 7
    while len(new_id_list) <= 2:
        new_id_list.append(new_id_list[-1]) 
    return "".join(new_id_list)