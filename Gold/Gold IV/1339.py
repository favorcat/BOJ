import sys
input = sys.stdin.readline

n = int(input())
word = [input().rstrip() for _ in range(n)]
dic = {}
idx = 9
ans = 0

for a in word:
  for j in range(len(a)):
    tmp = 10 ** (len(a) - j - 1)
    if a[j] in dic:
      dic[a[j]] += tmp
    else: dic[a[j]] = tmp
sdic = sorted(dic.items(), key=lambda x: -x[1])

for i in sdic:
  ans += i[1] * idx
  idx -= 1
print(ans)
