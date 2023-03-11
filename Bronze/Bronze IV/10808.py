s = list(input())
li = [0] * 26
for a in s:
  li[ord(a)-97] += 1
for n in li:
  print(n, end=" ")
