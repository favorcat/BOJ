n = int(input())
card = {}
for _ in range(n):
  a = int(input())
  card.setdefault(a, 0)
  card[a] += 1

ans = sorted(card.items(), key=lambda x : (-x[1],x[0]))
print(ans[0][0])