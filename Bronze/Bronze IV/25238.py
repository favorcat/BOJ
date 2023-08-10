import sys
input = sys.stdin.readline
a, b= map(int,input().split())

monster = a * (100-b) / 100
if monster < 100: print(1)
else: print(0)