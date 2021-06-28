N = input()
M = [int(i) for i in N]

M.sort(reverse=True)
for i in M:
    print(i, end="")