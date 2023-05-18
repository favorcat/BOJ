import math
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  ans = ""
  letter = input().rstrip()
  m = int(math.sqrt(len(letter)))
  for i in range(m):
    for k in range(m):
      ans += letter[m*k + m - i - 1]
  print(ans)