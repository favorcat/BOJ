n = int(input())
li = map(int,input().split())
for a in sorted(list(set(li))):
  print(a, end=" ")