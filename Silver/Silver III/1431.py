n = int(input())
serial = [input() for _ in range(n)]

def cal(a):
  cnt = 0
  for m in a:
    if m.isdigit():
      cnt+=int(m)
  return cnt
serial.sort(key= lambda x:(len(x), cal(x), x))

for i in serial:
  print(i)