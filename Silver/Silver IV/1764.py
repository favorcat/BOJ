import sys
N, M = map(int, sys.stdin.readline().split())
nohear = []
nolook = []
nohearlook = []

for i in range(N):
    nohear.append(sys.stdin.readline().strip())
for i in range(M):
    nolook.append(sys.stdin.readline().strip())

nohearlook = sorted(list(set(nohear) & set(nolook)))

print(len(nohearlook))
for name in nohearlook:
    print(name)