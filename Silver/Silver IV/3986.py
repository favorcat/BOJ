n = int(input())
ans = 0

for _ in range(n):
  s = input().rstrip()
  stack = []
  for i in range(len(s)):
    if stack and stack[-1] == s[i]:
      stack.pop()
    else:
      stack.append(s[i])
  if not stack:
    ans += 1
print(ans)