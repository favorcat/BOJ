import sys
input = sys.stdin.readline
n = int(input())
ans = ''

if n == 0:
  print(0)
  exit()

while n:
  if n % (-2):
    ans = '1' + ans
    n = n//(-2) + 1
  else:
    ans = '0' + ans
    n = n//(-2)

print(ans)