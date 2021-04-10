m = list(map(int,input().split()))
asc = sorted(m)
des = sorted(m, reverse=True)

if (m == asc): print('ascending')
elif (m == des): print('descending')
else: print('mixed')
