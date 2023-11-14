n = input()
ans = 0

for i in range(1, len(n)):
  s1, s2 = n[:i], n[i:]
  a1, a2 = 1, 1
  for j in s1:
    a1 *= int(j)
  for j in s2:
    a2 *= int(j)
  if a1 == a2:
    ans = i
    break
print("YES" if ans else "NO")