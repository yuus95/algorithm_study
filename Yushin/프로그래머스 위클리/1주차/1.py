price =3
money = 20
count = 4

def solution(price, money, count):
    req_moeny = [price * i for i in range(1,count+1)]
    answer= (sum(req_moeny) - money) if sum(req_moeny) > money else 0


    return answer


print(solution(price,money,count))