n = int(input())
chat = set()
ans = 0
for _ in range(n):
  a = input()
  if a == 'ENTER':
    ans += len(chat)
    chat.clear()
  else:
    chat.add(a)
ans += len(chat)
print(ans)