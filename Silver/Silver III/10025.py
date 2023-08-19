import sys
input = sys.stdin.readline
n, k = map(int,input().split())
ice = [0] * 1000001
end = 0

for _ in range(n):
  g, x = map(int,input().split())
  ice[x] = g
  end = max(end, x)

start = 2*k + 1
tmp = sum(ice[:start])
ans = tmp

for i in range(start, end+1):
  tmp += ice[i] - ice[i-start]
  ans = max(ans, tmp)
print(ans)