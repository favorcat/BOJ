import sys
input = sys.stdin.readline

N,L = map(int,input().split())
loca = list(map(int,input().split()))
loca.sort()

tmp = 0
cnt = 0
for i in range(N):
  if loca[i] > tmp:
    tmp = loca[i]+L-1
    cnt += 1
print(cnt)
