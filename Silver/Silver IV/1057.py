n,start,end = map(int, input().split())
ans = 0
while start != end:
  start -= start//2
  end -= end//2
  ans += 1
print(ans)