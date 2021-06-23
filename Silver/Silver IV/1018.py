N, M = map(int,input().split())
board = []
for i in range(N):
    board.append(input())
repair = []

for i in range(N-7):
    for j in range(M-7):
        W = 0
        B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        W += 1
                    if board[k][l] != 'B':
                        B += 1
                else:
                    if board[k][l] != 'B':
                        W += 1
                    if board[k][l] != 'W':
                        B += 1
        repair.append(W)
        repair.append(B)

print(min(repair))