n = int(input())
f = int(input())
ans = n // 100 * 100
while ans % f != 0:
  ans += 1
print(str(ans)[-2:])