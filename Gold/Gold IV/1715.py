import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
heapq.heapify(arr)
ans = 0

while len(arr) > 1:
  tmp = heapq.heappop(arr) + heapq.heappop(arr)
  heapq.heappush(arr, tmp)
  ans += tmp

print(ans)
