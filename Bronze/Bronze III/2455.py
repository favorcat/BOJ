ans = []
tmp = 0
for _ in range(4):
  a,b = map(int,input().split())
  tmp += b - a
  ans.append(tmp)
print(max(ans))