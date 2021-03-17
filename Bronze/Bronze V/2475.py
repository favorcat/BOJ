n = list(map(int,input().split()))
a = 0
for i in range(5):
    a += n[i] * n[i]
print(a % 10)
