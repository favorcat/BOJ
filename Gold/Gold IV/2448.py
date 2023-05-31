import sys
input = sys.stdin.readline
n = int(input())
star = [[' ' for _ in range(n*2)] for _ in range(n)]

def create(c, r, size):
  if size == 3:
    star[c][r] = "*"
    star[c+1][r-1] = star[c+1][r+1] = '*'
    for i in range(-2, 3):
      star[c+2][r-i] = '*'
  else:
    size2 = size//2
    create(c, r, size2)
    create(c+size2, r-size2, size2)
    create(c+size2, r+size2, size2)
create(0, n-1, n)

for s in star:
  print("".join(s))