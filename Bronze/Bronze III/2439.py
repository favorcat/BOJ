n = int(input())
for i in range (n):
    for k in range(1, n-i):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print('')