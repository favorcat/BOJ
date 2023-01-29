import sys
n, m =map(int,sys.stdin.readline().split())
dic = {}
for _ in range(n):
  site, pw = map(str,sys.stdin.readline().split())
  dic[site] = pw
for _ in range(m):
  site = input()
  print(dic[site])
