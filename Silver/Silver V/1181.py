n = int(input())
m = []

for i in range(n):
    word = str(input())
    length = len(word)
    m.append((length, word))

m = list(set(m))
m.sort()

for length, word in m:
    print(word)