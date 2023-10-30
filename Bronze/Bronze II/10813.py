n, m = map(int,input().split())
ball = [i for i in range(1, n+1)]
for _ in range(m):
  i, j = map(int,input().split())
  ball[i-1], ball[j-1] = ball[j-1], ball[i-1]
print(*ball)