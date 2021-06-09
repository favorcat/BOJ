n = int(input())
m = int(input())
remote = {str(i) for i in range(10)}
if m != 0:
    remote -= set(map(str, input().split()))

count = abs(100-n)
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in remote:
            break
        elif j == len(num) - 1:
            count= min(count, abs(n - int(num)) + len(str(num)))
print(count)