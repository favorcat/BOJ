import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()

dic = {}
left = 0
ans = 0

for i in range(len(s)):
  dic.setdefault(s[i], 0)
  dic[s[i]] += 1
  while len(dic) > n:
    dic[s[left]] -= 1
    if dic[s[left]] == 0:
      del dic[s[left]]
    left += 1
  ans = max(ans, i-left+1)
print(ans)