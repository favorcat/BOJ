from sys import stdin
for i in range(3):
    n = int(stdin.readline())
    s = 0
    for k in range(n):
        s += int(stdin.readline())
    if s == 0: print("0")
    elif s > 0: print("+")
    else: print("-")
