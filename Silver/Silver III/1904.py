N = int(input())
arr = [0] * 1000001
arr[1] = 1
arr[2] = 2

for i in range(N+1):
    if i > 2:
        arr[i] = (arr[i-1] + arr[i-2]) % 15746

print(arr[N])