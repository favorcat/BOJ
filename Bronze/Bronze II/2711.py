T = int(input())
for _ in range(T):
    n, s = map(str,input().split())
    n = int(n)
    s = list(s)
    s.pop(n-1)
    print(''.join(s))
