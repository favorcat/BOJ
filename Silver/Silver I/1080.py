import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
A = [list(map(int, input().rstrip())) for _ in range(n)]
B = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0

def change(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      A[i][j] = 1 - A[i][j]

for i in range(n-2):
  for k in range(m-2):
    if A[i][k] != B[i][k]:
      change(i, k)
      cnt += 1

for i in range(n):
  for k in range(m):
    if A[i][k] != B[i][k]:
      cnt = -1
      break

print(cnt)