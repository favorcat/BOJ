N = int(input())
for i in range(N):
    R, S = input().split()
    res = ''
    for k in range(len(S)):
        res += int(R)*S[k]
    print(res)
