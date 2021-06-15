A, B, C = map(int,input().split())
min_num = min(B, C)
if B == min_num:
    print(int(A/B*C))
else:
    print(int(A*B/C))