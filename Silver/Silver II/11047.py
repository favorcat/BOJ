N, K = map(int,input().split())
coin = []
ans = 0
for i in range(N):
    coin.append(int(input()))
    
coin.sort(reverse=True)
for num in coin:
    if K == 0: break
    ans += K//num
    K %= num

print(ans)