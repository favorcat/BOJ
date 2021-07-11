T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    Y = 0
    X = 0
    if N % H == 0:
        Y = H
        X = N // H
    else:
        Y = N % H
        X = N // H + 1
    print(Y*100 + X)