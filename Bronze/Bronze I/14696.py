n = int(input())
for _ in range(n):
  a = list(map(int, input().split()))[1:]
  b = list(map(int, input().split()))[1:]
  
  for i in range(4,0,-1):
    if a.count(i) > b.count(i):
      print("A")
      break
    elif a.count(i) < b.count(i):
      print("B")
      break
    if i == 1:
      print("D")