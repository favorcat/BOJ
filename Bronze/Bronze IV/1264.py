while True:
  s = input()
  if s == "#":
    break
  cnt = 0
  for a in s:
    if a in ['a','e','i','o','u','A','E','I','O','U']:
      cnt += 1
  print(cnt)
