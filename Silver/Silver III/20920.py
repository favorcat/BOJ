import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
li = {}

for _ in range(n):
  word = input().rstrip()
  if len(word) < m:
    continue
  else:
    if word in li:
      li[word] += 1
    else:
      li[word] = 1

li = sorted(li.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in li:
    print(i[0])