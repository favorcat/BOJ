t = int(input())
for _ in range(t):
  n = int(input())
  cnt = 0
  ans = ''
  for _ in range(n):
    name, acl = map(str,input().split())
    if int(acl) > cnt:
      cnt = int(acl)
      ans = name
  print(ans)