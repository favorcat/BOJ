reca = {}
recb = {}
for _ in range(3):
  a, b = map(str,input().split())
  if a not in reca:
    reca[a] = 1
  else:
    reca[a] += 1

  if b not in recb:
    recb[b] = 1
  else:
    recb[b] += 1

for key, val in reca.items():
  if val == 1 or val == 3:
    print(key, end=" ")
for key, val in recb.items():
  if val == 1 or val == 3:
    print(key, end=" ")
