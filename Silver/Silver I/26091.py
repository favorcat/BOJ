import sys
input = sys.stdin.readline
n, m = map(int,input().split())
student = list(map(int, input().split()))
student.sort(key=lambda x: x)

cnt = 0
for i in range(n//2):
  if student[i] + student[n-i-1] >= m:
    cnt += 1
print(cnt)