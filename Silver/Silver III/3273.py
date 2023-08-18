n = int(input())
li = list(map(int,input().split()))
x = int(input())
li.sort()

left = 0
right = n-1
ans = 0

while left < right:
  tmp = li[left]+li[right]
  if tmp == x: ans += 1
  if tmp < x:
    left += 1
    continue
  right -= 1
print(ans)