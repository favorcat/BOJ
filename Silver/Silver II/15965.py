n = 10 ** 7
arr = [1] * n

for i in range(2, int(n**0.5) + 1):
    if arr[i]:
        for j in range(i+i, n, i):
            arr[j] = 0
prime = [i for i in range(2, n) if arr[i]]

K = int(input())
print(prime[K-1])