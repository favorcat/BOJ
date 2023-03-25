import sys
input = sys.stdin.readline

S = input().rstrip()
dic = {}

for a in S:
  if a in dic:
    dic[a] += 1
  else: dic[a] = 1
dic = sorted(dic.items(), key=lambda x: x[0])

cnt = 0
for i in dic:
  if i[1]%2 == 1:
    cnt += 1

if len(S)%2 == 1 and (cnt > 1 or cnt == 0):
  print("I'm Sorry Hansoo")
elif len(S)%2 == 0 and cnt > 0:
  print("I'm Sorry Hansoo")
else:
  ans = ""
  cen = ""
  for i in dic:
    if i[1]%2 == 1:
      cen = i[0]
    ans += i[0] * (i[1]//2)
  print(ans + cen + ans[::-1])