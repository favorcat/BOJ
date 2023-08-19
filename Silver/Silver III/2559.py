import sys
input = sys.stdin.readline
n, k = map(int,input().split())
li = list(map(int,input().split()))

ans = [sum(li[:k])]

for i in range(0, n-k):
  ans.append(ans[i] - li[i] + li[i+k])
print(max(ans))