import sys
input = sys.stdin.readline
a = input().rstrip()
ans = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in range(len(a)):
    for d in dial:
        if a[i] in d:
            ans += dial.index(d)+3
print(ans)