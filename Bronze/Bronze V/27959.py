import sys
input = sys.stdin.readline
n, m = map(int,input().split())
if n*100 >= m: print("Yes")
else: print("No")