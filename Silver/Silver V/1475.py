N = input()
num = [0 for i in range(9)]
six = 0

for i in range(len(N)):
    if N[i] in ['6', '9']:
        six += 1
    else:
        num[int(N[i])] += 1

if six % 2 == 0:
    six //= 2
else:
    six += 1
    six //= 2

num[6] = six
print(max(num))