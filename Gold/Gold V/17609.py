import sys
input = sys.stdin.readline
t = int(input())

def check(x, left, right):
  while left < right:
    if x[left] == x[right]:
      left += 1
      right -= 1
    else:
      return False
  return True

for _ in range(t):
  s = input().rstrip()
  ans = 0
  if s == s[::-1]:
    ans = 0
  else:
    left = 0
    right = len(s)-1
    while left < right:
      if s[left] == s[right]:
        left += 1
        right -= 1
      else:
        if check(s, left+1, right) or check(s, left, right-1):
          ans = 1
          break
        else:
          ans = 2
          break
  print(ans)