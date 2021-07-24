import sys
N, M, B = map(int, sys.stdin.readline().split())
house = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
height = 0
time = 100000000000000
for i in range(257):
    max_height = 0
    min_height = 0
    for j in range(N):
        for k in range(M):
            if house[j][k] < i:
                min_height += (i - house[j][k])
            else:
                max_height += (house[j][k] - i)
        inventory = max_height + B
    if inventory < min_height:
        continue
    t = min_height + 2 * max_height
    if t <= time:
        time = t
        height = i
print(time, height)