import math
n, k = map(int,input().split())

if k<0 or k>n:
    print(0)
else:
    print(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))