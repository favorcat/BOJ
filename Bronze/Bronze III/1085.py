x, y, w, h = map(int,input().split())
arr = [x, y, w-x, h-y]
ans = x
for i in range(4):
    if ans > arr[i]: ans = arr[i]
print(ans)