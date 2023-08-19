import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = a + b
ans.sort()
print(" ".join(map(str,ans)))