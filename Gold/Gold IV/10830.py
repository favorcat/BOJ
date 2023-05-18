import sys
input = sys.stdin.readline
n,b = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def mul(q, w):
      l = len(q)
      e = [[0]*l for _ in range(n)]
      
      for i in range(n):
            for k in range(n):
                  p = 0
                  for j in range(n):
                        p += q[i][j] * w[j][k]
                  e[i][k] = p % 1000
      return e


def cal(a, b):
      if b == 1:
            for x in range(len(a)):
                  for y in range(len(a)):
                        a[x][y] %= 1000
            return a
      
      tmp = cal(a, b//2)
      if b % 2:
            return mul(mul(tmp, tmp), a)
      else:
            return mul(tmp, tmp)

ans = cal(a, b)

for i in range(n):
      for k in range(n):
            print(ans[i][k], end=" ")
      print()