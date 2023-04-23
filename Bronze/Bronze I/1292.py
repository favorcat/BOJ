import sys
input = sys.stdin.readline
a, b = map(int,input().split())

arr = [0]
for i in range(1, b+1):
  for k in range(i):
    arr.append(i)

sum = 0
for i in range(a, b+1):
  sum += arr[i]
print(sum)