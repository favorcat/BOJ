import sys
input = sys.stdin.readline
n, b = map(int,input().split())

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

while n:
  ans += str(a[n % b])
  n //= b
print(ans[::-1])