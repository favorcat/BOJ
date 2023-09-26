target_numbers = [202021, 20202021, 202002021, 202012021, 202022021, 202032021, 202042021, 202052021, 202062021, 202072021, 202082021, 202092021]

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    ans = 0
    for num in arr:
        for target in target_numbers:
            complement = target - num
            if complement in freq:
                ans += freq[complement]
                if complement == num:
                    ans -= 1
    print(ans // 2)