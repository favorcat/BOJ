while True:
    tr = list(map(int,input().split()))
    tr.sort()
    if (tr[0] == 0) : break
    if ((tr[0]**2+tr[1]**2) == tr[2]**2):
        print('right')
    else: print('wrong')