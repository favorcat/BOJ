x, y = map(int,input().split())
z = (y*100)/x
left = 0
right = x
ans = x
if z >= 99:
  ans = -1
else:
  while left <= right:
    mid = (left+right)//2
    if ((y+mid)*100)//(x+mid) > z:
      ans = mid
      right = mid-1
    else:
      left = mid+1
print(ans)