import sys
input = sys.stdin.readline
n = int(input())
work = [list(map(int,input().split())) for _ in range(n)]
work.sort(key=lambda x: x[1], reverse=True)

answer = work[0][1]
for i in range(n):
  answer = min(work[i][1], answer) - work[i][0]
print(answer)