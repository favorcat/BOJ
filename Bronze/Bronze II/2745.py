n, b = map(str,input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = n[::-1]
ans = 0
for i, v in enumerate(n):
  ans += arr.index(v) * (int(b)**i)
print(ans)