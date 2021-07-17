def solution(record):
    answer = []
    result = []
    for i in record:
        list_record = list(i.split(" "))
        if list_record[0] == 'Change':
            for j in result:
                if j[0] == 'Enter' and list_record[1] in j:
                    j[2] = list_record[2]
        elif list_record[0] == 'Leave':
            result.append(['Leave',list_record[1]])
        elif list_record[0] == 'Enter':
            for j in result:
                if j[0] == 'Enter' and list_record[1] in j:
                    j[2] = list_record[2]
            result.append(['Enter',list_record[1], list_record[2]])
    print(result)                
    
    for i in result:
        if i[0] == 'Enter':
            answer.append(i[2]+'님이 들어왔습니다.')
        elif i[0] == 'Leave':
            for j in result:
                if i[1] in j and j[0]=='Enter':
                    demo = j[2]
            answer.append(j[2]+'님이 나갔습니다.')        
            
    
    return answer