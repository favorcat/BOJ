import sys
input = sys.stdin.readline

n, m = map(int,input().split())
li = list(map(int,input().split()))

left = 0
right = 0
cnt = [0] * (max(li)+1)
ans = 0

while right < n:
  if cnt[li[right]] >= m:
    cnt[li[left]] -= 1
    left += 1
  else:
    cnt[li[right]] += 1
    right += 1
    ans = max(ans, right-left)
print(ans)