n, k = map(int, input().split())
li = list(map(int, input().split(',')))
for _ in range(k):
    t = [li[i+1]-li[i] for i in range(len(li)-1)]
    li = t
print(*li, sep=',')