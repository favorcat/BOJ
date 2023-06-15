import sys
input = sys.stdin.readline
ans = 0
li = [int(input()) for _ in range(10)]

for n in li:
  ans += n
  if ans >= 100:
    if ans - 100 > 100 - (ans-n):
      ans -= n
    break
print(ans)