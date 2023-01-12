def star(n):
  if n==1: return "*"
  stars = star(n//3)
  arr = []
  for s in stars: arr.append(s*3) #윗줄
  for s in stars: arr.append(s+" "*(n//3)+s) #중간줄
  for s in stars: arr.append(s*3) #아랫줄
  return arr

n = int(input())
print('\n'.join(star(n)))
