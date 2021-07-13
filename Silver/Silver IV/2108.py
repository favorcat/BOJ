import sys
N = int(sys.stdin.readline())
number = []
arr = [0] * 8001
for i in range(N):
    m = int(sys.stdin.readline())
    number.append(m)
    arr[m+4000] += 1

sorted_number = sorted(number)
check = 0
big = max(arr)
for i in range(len(arr)):
    if arr[i] == big:
        if check == 0:
            check = 1
            common_index = i - 4000
        elif check == 1:
            check = 2
            common_index = i - 4000
            break

print(round(sum(number)/N))
print(sorted_number[N//2])
print(common_index)
print(max(number)-min(number))