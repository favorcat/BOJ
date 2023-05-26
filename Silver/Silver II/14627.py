import sys
input = sys.stdin.readline
s, c = map(int,input().split())
pa = [int(input()) for _ in range(s)]

left, right = 1, max(pa)
while left <= right:
  mid = (left + right) // 2
  tmp = sum(i//mid for i in pa)
  if tmp >= c:
    left = mid + 1
  else:
    right = mid - 1

answer = sum(pa) - (right * c)
print(answer)