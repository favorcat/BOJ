import math
import sys
input = sys.stdin.readline
n, k = map(int,input().split())

res = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(res % 10007)