import sys
input = sys.stdin.readline
n, s = map(int,input().split())
li = list(map(int,input().split()))

left = 0
right = 0
tmp = li[0]
ans = 100001

while True:
  if tmp >= s:
    tmp -= li[left]
    ans = min(ans, right-left+1)
    left += 1
  else:
    right += 1
    if right == n:
      break
    tmp += li[right]

if ans == 100001: print(0)
else: print(ans)