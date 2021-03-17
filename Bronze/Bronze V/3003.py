chess = list(map(int,input().split()))
for i in range(len(chess)):
    if i <= 1:
        print(1-chess[i], end=' ')
    elif 2<= i <= 4:
        print(2-chess[i], end=' ')
    else:
        print(8-chess[i], end=' ')

'''
chess = list(map(int,input().split()))
print(1-chess[0], end=' ')
print(1-chess[1], end=' ')
print(2-chess[2], end=' ')
print(2-chess[3], end=' ')
print(2-chess[4], end=' ')
print(8-chess[5])
'''
