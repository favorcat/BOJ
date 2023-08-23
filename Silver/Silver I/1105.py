import sys
input = sys.stdin.readline
L, R = map(str,input().split())

ans = 0
if len(L) == len(R):
  for i in range(len(L)):
    if L[i] == R[i]:
      if L[i] == '8':
        ans += 1
    else:
      break
print(ans)