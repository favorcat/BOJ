import math
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = math.factorial(n)
b = math.factorial(m)*math.factorial(n-m)
print(a//b)