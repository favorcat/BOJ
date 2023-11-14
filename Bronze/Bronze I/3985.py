L = int(input())
N = int(input())

li = [0 for _ in range(L+1)]
mx = 0
mx_i = 0
for i in range(N):
  P, K = map(int, input().split())
  if K-P > mx:
    mx = K-P
    mx_i = i+1
  for j in range(P, K+1):
    if li[j] == 0:
      li[j] = i+1
print(mx_i)

ans = 0
ans_i = 0
for i in range(1, N+1):
  tmp = li.count(i)
  if tmp > ans:
    ans = tmp
    ans_i = i
print(ans_i)