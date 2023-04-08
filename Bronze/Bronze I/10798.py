s = [input() for _ in range(5)]
for i in range(15):
  for k in range(5):
    if i < len(s[k]):
      print(s[k][i], end="")
