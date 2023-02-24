emoji = input()

n = len(emoji) + 2
cnt = 0
for s in emoji:
  if s == '_':
    cnt += 1

print(n+cnt*5)