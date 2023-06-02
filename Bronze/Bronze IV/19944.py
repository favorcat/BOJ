n, m = map(int,input().split())
if m <= 2: print("NEWBIE!")
elif m <= n and m > 2: print("OLDBIE!")
else: print("TLE!")