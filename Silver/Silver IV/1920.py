n = int(input())
a = set(map(int,input().split()))
m = int(input())
ma = list(map(int,input().split()))

for i in range (m):
    print(int(ma[i] in a))
