import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  a,b = map(str,input().split())
  a2 = sorted(list(a))
  b2 = sorted(list(b))
  if a2 == b2:
    print(a,"&",b,"are anagrams.")
  else:
    print(a,"&",b,"are NOT anagrams.")