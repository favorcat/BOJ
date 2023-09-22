import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
op = list(map(int, input().split()))

mx = -1e9+1
mn = 1e9+1
def dfs(depth, total, plus, minus, mul, div):
  global mx, mn
  if depth == n:
    mx = max(mx, total)
    mn = min(mn, total)
    return
  
  if plus:
    dfs(depth + 1, total + m[depth], plus - 1, minus, mul, div)
  if minus:
    dfs(depth + 1, total - m[depth], plus, minus - 1, mul, div)
  if mul:
    dfs(depth + 1, total * m[depth], plus, minus, mul - 1, div)
  if div:
    dfs(depth + 1, int(total / m[depth]), plus, minus, mul, div - 1)
dfs(1, m[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)