n = int(input())
ln = len(str(n))
ans = 0
for i in range(ln-1):
    ans += (i+1) * (9 * 10 ** i)
ans += (ln) * (n - 10 ** (ln-1) + 1)
print(ans)
