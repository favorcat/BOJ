import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

while start<=end:
    height = (start+end)//2
    num = 0
    for i in tree:
        num += i - height if i - height > 0 else 0
    if num >= m: start = height + 1
    else: end = height -1

print(end)