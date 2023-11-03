n, m = map(int,input().split())
basket = [i for i in range(1, n+1)]
for _ in range(m):
  i, j = map(int,input().split())
  tmp = basket[i-1:j]
  tmp.reverse()
  basket[i-1:j] = tmp
print(*basket)