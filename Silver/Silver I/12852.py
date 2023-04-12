import sys
input = sys.stdin.readline

n = int(input())
cnt = [[0,[]] for _ in range(n+1)]
cnt[1][0] = 0
cnt[1][1] = [1]

for i in range(2, n+1):
    cnt[i][0] = cnt[i-1][0] + 1
    cnt[i][1] = cnt[i-1][1] + [i]
    if i%2 == 0 and cnt[i][0] > cnt[i//2][0] + 1:
        cnt[i][0] = cnt[i//2][0] + 1
        cnt[i][1] = cnt[i//2][1] + [i]
    if i%3 == 0 and cnt[i][0] > cnt[i//3][0] + 1:
        cnt[i][0] = cnt[i//3][0] + 1
        cnt[i][1] = cnt[i//3][1] + [i]
print(cnt[n][0])
print(*cnt[n][1][::-1])