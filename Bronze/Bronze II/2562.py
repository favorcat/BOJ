m = []

for i in range(9):
    k = int(input())
    m.append((k, i))

m.sort()

print(m[8][0])
print(m[8][1]+1)