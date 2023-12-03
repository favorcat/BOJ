import sys
input = sys.stdin.readline
n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0

def check():
  global ans
  for i in range(n):
    cnt = 1
    for j in range(1, n):
      if board[i][j] == board[i][j-1]:
        cnt += 1
        ans = max(ans, cnt)
      else:
        cnt = 1
    cnt = 1
    for j in range(1, n):
      if board[j][i] == board[j-1][i]:
        cnt += 1
        ans = max(ans, cnt)
      else:
        cnt = 1

for i in range(n):
  for j in range(n):
    if j+1<n:
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      check()
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    if i+1<n:
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      check()
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(ans)