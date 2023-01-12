x, y = map(str, input().split())

def Rev(n):
  res = ""
  for i in range(len(n)):
    res += n[len(n)-i-1]
  return int(res)

print(Rev(str(Rev(x) + Rev(y))))
