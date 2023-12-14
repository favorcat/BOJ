from collections import defaultdict
n = int(input())
sell = defaultdict(int)

for i in range(n):
  book = input()
  sell[book] += 1

sell = sorted(sell.items())
print(sorted(sell, key = lambda x:x[1], reverse=True)[0][0])