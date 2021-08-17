def solution(record):
    answer = []
    result = {}
    
    for i in record:
        list_record = i.split(" ")
        if list_record[0] == 'Enter' or list_record[0] =='Change':
            result[list_record[1]] = list_record[2]
    
    for i in record:
        list_record = i.split(" ")
        if list_record[0] == 'Enter':
            answer.append(result[list_record[1]] + "님이 들어왔습니다.")
        elif list_record[0] == 'Leave':
            answer.append(result[list_record[1]] + "님이 나갔습니다.")

    return answer