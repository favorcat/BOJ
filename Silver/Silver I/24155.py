import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  members = [list(map(int, input().split())) for _ in range(n)]
  members.sort(key=lambda x: x[0])
  cnt = 1
  tmp = members[0][1]

  for i in range(n):
    if tmp > members[i][1]:
      tmp = members[i][1]
      cnt += 1
  print(cnt)
