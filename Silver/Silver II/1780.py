import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
ans1 = 0
ans2 = 0
ans3 = 0

def dfs(x,y,n):
  global ans1, ans2, ans3
  tmp = li[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if li[i][j] != tmp:
        for k in range(3):
          for l in range(3):
            dfs(x+k*n//3, y+l*n//3, n//3)
        return
  if tmp == -1:
    ans1 += 1
  elif tmp == 0:
    ans2 += 1
  elif tmp == 1:
    ans3 += 1

dfs(0,0,n)
print(ans1)
print(ans2)
print(ans3)