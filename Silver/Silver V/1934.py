T = int(input())

def LCM(A, B):
    gcd = GCD(A, B)
    return int((A * B) / gcd)

def GCD(A, B):
    return GCD(B%A, A) if B%A else A

for i in range(T):
    A, B = map(int,input().split())
    print(LCM(A, B))