import sys
input = sys.stdin.readline

a, b = map(int,input().split())
n_min = min(a,b)
n_max = max(a,b)
n = n_max - n_min

print((n*(n+1))//2 + (n_min * (n+1)))
