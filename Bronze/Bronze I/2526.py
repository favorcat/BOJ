n, p = map(int,input().split())
li = []
tmp = n

while True:
  tmp = (tmp*n)%p
  if tmp in li:
    print(len(li) - li.index(tmp))
    break
  li.append(tmp)