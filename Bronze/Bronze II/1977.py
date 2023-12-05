m = int(input())
n = int(input())
ans_sum = 0
ans_min = 0

for i in range(1, 101):
    if m <= i*i and n >= i*i:
        if ans_sum == 0:
            ans_min = i*i
        ans_sum += i*i

if ans_sum == 0:
    print(-1)
else:
    print(ans_sum)
    print(ans_min)