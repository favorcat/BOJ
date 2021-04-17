from collections import deque
n = int(input())
arr = deque([i for i in range(1,n+1)])
while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
print(arr.pop())