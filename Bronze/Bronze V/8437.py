import sys
input = sys.stdin.readline
n = int(input())
gap = int(input())

tmp = (n - gap) // 2
a, b = tmp + gap, tmp
print(a)
print(b)