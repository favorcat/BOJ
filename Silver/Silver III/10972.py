import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if li[i-1] < li[i]:
        for j in range(n-1, 0, -1):
            if li[i-1] < li[j]:
                li[i-1], li[j] = li[j], li[i-1]
                li = li[:i] + sorted(li[i:])
                print(*li)
                exit()
print(-1)