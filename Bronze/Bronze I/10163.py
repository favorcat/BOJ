graph = [[0 for _ in range(1001)] for _ in range(1001)]
n = int(input())

for p in range(1, n+1):
    p_x, p_y, w, h = map(int, input().split())
    for y in range(p_y, p_y+h):
        graph[y][p_x:(p_x+w)] = [p]*w
            
for p in range(1, n+1):
    ans = 0
    for cnt in range(1001):
        ans += graph[cnt].count(p)
    print(ans)