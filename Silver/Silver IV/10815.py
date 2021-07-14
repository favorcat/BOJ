import sys
n = int(sys.stdin.readline())
card = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_card = list(map(int,sys.stdin.readline().split()))
result = [0] * m

for i in range(m):
    if check_card[i] in card:
        result[i] = 1

for check in result:
    print(check, end=' ')