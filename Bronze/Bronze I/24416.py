import sys
input = sys.stdin.readline
n = int(input())

def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

def fibbonacci(n):
  dp = [0] * (n+1)
  dp[1] = 1
  dp[2] = 1
  cnt = 0
  for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    cnt += 1
  return cnt

print(fib(n), fibbonacci(n))