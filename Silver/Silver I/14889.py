n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
visited = [False] * n

def dfs(depth, idx):
    global ans
    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += s[i][j]
                elif not visited[i] and not visited[j]:
                    link += s[i][j]
        ans = min(ans, abs(start - link))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(ans)
