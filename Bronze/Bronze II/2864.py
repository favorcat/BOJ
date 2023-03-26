import sys
input = sys.stdin.readline

a,b = map(str,input().split())

mina = 0
minb = 0
maxa = 0
maxb = 0

for i in range(len(a)):
  if a[i] == "6" or a[i] == "5":
    mina += 5 * 10 ** (len(a)-i-1)
    maxa += 6 * 10 ** (len(a)-i-1)
  else:
    mina += int(a[i]) * 10 ** (len(a)-i-1)
    maxa += int(a[i]) * 10 ** (len(a)-i-1)

for j in range(len(b)):
  if b[j] == "6" or b[j] == "5":
    minb += 5 * 10 ** (len(b)-j-1)
    maxb += 6 * 10 ** (len(b)-j-1)
  else:
    minb += int(b[j]) * 10 ** (len(b)-j-1)
    maxb += int(b[j]) * 10 ** (len(b)-j-1)

print(mina+minb,maxa+maxb)