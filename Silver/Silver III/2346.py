from collections import deque

n = int(input())
q = deque(enumerate(map(int,input().split())))
ans = []
while q:
    i, v = q.popleft()
    ans.append(i+1)
    if v > 0:
        q.rotate(-(v-1))
    elif v < 0:
        q.rotate(-v)
print(*ans)