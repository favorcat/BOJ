import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = sorted(map(int,input().split()))
left = 0
right = n-1
cnt = 0

while left != right:
  tmp = li[left]+li[right]
  if tmp == m:
    cnt += 1
    left += 1
  elif tmp > m:
    right -= 1
  else:
    left += 1

print(cnt)