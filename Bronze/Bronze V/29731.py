n = int(input())
a = [
      "Never gonna give you up",
      "Never gonna let you down",
      "Never gonna run around and desert you",
      "Never gonna make you cry",
      "Never gonna say goodbye",
      "Never gonna tell a lie and hurt you",
      "Never gonna stop"
]
ans = 1
for _ in range(n):
  s = input().rstrip()
  if s not in a:
    ans = 0
    break
if ans == 0:
  print("Yes")
else:
  print("No")