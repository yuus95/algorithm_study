def solution(numbers, hand):
    phone = [1,2,3,4,5,6,7,8,9,'*',0,'#']
    result = {}
    answer = ''
    for i in range(len(phone)):
        col = i % 3
        row = i // 3
        result[phone[i]] = [row,col]
    left_x = 3
    left_y = 0
    right_x = 3
    right_y = 2
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            x,y = result[i]
            left_x = x
            left_y = y
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            x,y = result[i]
            right_x = x
            right_y = y
            answer += 'R'
        else:
            x,y = result[i]
            
            left_n = abs(x - left_x) + abs(y - left_y)
            right_n = abs(x - right_x) + abs(y - right_y)
            
            if left_n == right_n:
                if hand == 'right':
                    answer += 'R'
                    right_x = x
                    right_y = y
                else:
                    answer += 'L'
                    left_x = x
                    left_y = y
            elif left_n > right_n:
                answer += 'R'
                right_x = x
                right_y = y
            else:
                answer += 'L'
                left_x = x
                left_y = y
        
    
    return answer