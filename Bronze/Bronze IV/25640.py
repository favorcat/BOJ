import sys
input = sys.stdin.readline
mbti = input().rstrip()
n = int(input())
cnt = 0

for _ in range(n):
  a = input().rstrip()
  if a == mbti: cnt += 1

print(cnt)