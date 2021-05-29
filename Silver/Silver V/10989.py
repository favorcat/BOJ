import sys
n = int(sys.stdin.readline())
num = [0] * 10001
for i in range(n):
    num[int(sys.stdin.readline())] += 1
for i in range(10001):
    if num[i] != 0:
        for k in range(num[i]):
            print(i)