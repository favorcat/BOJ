k, n = map(int,input().split())
arr = [int(input()) for i in range(k)]

left = 1
right = max(arr)+1

while True:
    num = 0
    mid = (left+right)//2
    for m in arr:
        num += m//mid
    if num >= n:
        left = mid
    else:
        right = mid
    if right - left == 1:
        break

print(left)