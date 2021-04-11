while True:
    n = str(input())
    if (n == '0'): break
    com = ''.join(reversed(n))
    if (n==com): print('yes')
    else: print('no')