import heapq
import sys
input = sys.stdin.readline
n = int(input())
cls = [list(map(int,input().split())) for _ in range(n)]
cls.sort(key=lambda x: x[0])

q = []
heapq.heappush(q, cls[0][1])
for i in range(1, n):
  if cls[i][0] >= q[0]:
    heapq.heappop(q)
  heapq.heappush(q, cls[i][1])

print(len(q))