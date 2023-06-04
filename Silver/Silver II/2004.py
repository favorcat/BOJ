import sys
input = sys.stdin.readline
n, m = map(int,input().split())

def counting(x, y):
  cnt = 0
  while x > 0:
    cnt += x//y
    x //= y
  return cnt

cnt5 = counting(n, 5) - counting(m, 5) - counting(n-m, 5)
cnt2 = counting(n, 2) - counting(m, 2) - counting(n-m, 2)
print(min(cnt5, cnt2))