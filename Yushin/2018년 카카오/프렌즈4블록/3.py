def solution(m, n, board):
    answer = 0

    for i in range(len(board)):  # board 배열로 만들기
        popped = board.pop(0)
        board.append([p for p in popped])

    while True:  # 터진 블록이 없을 때까지 반복
        checked = []  # 이번 턴에 터져야 할 블록들 모음
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == "0":  # 이미 블록이 터져 빈 자리면 패스
                    continue
                if board[i][j] == board[i][j + 1]:  # 연속으로 두 개가 동일한 블록이면, 밑에 두 개도 동일한지 확인
                    if board[i][j] == board[i + 1][j] and board[i][j + 1] == board[i + 1][j + 1]:
                        checked.append((i, j))
                        checked.append((i, j + 1))
                        checked.append((i + 1, j))
                        checked.append((i + 1, j + 1))  # 터져야 할 블록들 전부 저장

        if len(checked) == 0:  # 이번에 터진 블록이 없으면 종료
            break
        else:
            answer += len(set(checked))  # 모아둔 블록 다 터뜨리기!
            for c in checked:
                board[c[0]][c[1]] = '0'

            for c in reversed(checked):  # 블록들 내리기
                check_n = c[0] - 1
                put_n = c[0]

                while check_n >= 0:  # 터진 자리 위에 있는 블록들을 다 내린다.
                    if board[put_n][c[1]] == "0" and board[check_n][c[1]] != "0":
                        board[put_n][c[1]] = board[check_n][c[1]]
                        board[check_n][c[1]] = "0"
                        put_n -= 1

                    check_n -= 1

    return answer

m= [4,6]
n = [5,6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"],["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]


for i in range(2):
    print(solution(m[i],n[i],board[i]))