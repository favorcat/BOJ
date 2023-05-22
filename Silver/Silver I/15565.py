import sys
input = sys.stdin.readline
n, k = map(int, input().split())
doll = list(map(int, input().split()))

answer = n + 1
left = 0
right = 0

if doll[0] == 1: cnt = 1
else: cnt = 0

while right < n:
  tmp = right - left + 1
  if cnt == k:
    answer = min(answer, tmp)
    if doll[left] == 1: cnt -= 1
    left += 1
  else:
    right += 1
    if right < n and doll[right] == 1: cnt += 1

if answer == n + 1: print(-1)
else: print(answer)