n = int(input())
li = [list(map(str, input().split())) for _ in range(n)]
li.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in li:
  print(s[0])
