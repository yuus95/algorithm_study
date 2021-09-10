def solution(numbers, hand):
    answer = ''
    key = {0:(3,1),1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

    lx,ly = 3,0
    rx,ry = 3,2

    for num in numbers:
        if num in (1,4,7):
           lx,ly = key[num]
           answer+="L"
        elif num in (3,6,9):
            rx,ry = key[num]
            answer +="R"
        else :
            x,y = key[num]
            ldis = abs(x-lx)+abs(y-ly)
            rdis = abs(x-rx)+abs(y-ry)

            if ldis > rdis :
                rx,ry = x,y
                answer +="R"
            elif ldis < rdis :
                lx,ly =  x,y
                answer+="L"
            else :
                if hand == "right":
                    rx,ry = x,y
                    answer +="R"
                else :
                    lx,ly = x,y
                    answer +="L"

    return answer

"LRLLRRLLLRR"
"LRLLRRLLLRR"


numbers = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]

hand =["right","left","right"]



for i in range(3):
    print(solution(numbers[i],hand[i]))
