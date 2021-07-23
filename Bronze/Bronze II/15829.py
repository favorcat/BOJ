import sys
L = int(sys.stdin.readline())
S = sys.stdin.readline()
hash = 0

if L == 1:
    hash = ord(S[0])-96
else:
    for i in range(L):
        n = ord(S[i])-96
        if i == 0:
            hash += n
        else:
            hash += n * 31 ** i

print(hash % 1234567891)