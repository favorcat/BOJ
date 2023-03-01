n = int(input())
result = {}
for _ in range(n):
  name, position = map(str, input().split())
  result[name] = position
result = dict(sorted(result.items(), reverse=True))

for key in result.copy().keys():
  if result[key] == 'leave':
    del(result[key])
  else:
    print(key)
