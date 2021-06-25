first_number = set(range(1,10000))
made_number = set()

for i in range(1, 10001):
    for k in str(i):
        i += int(k)
    made_number.add(i)

self_number = sorted(first_number - made_number)
for i in self_number:
    print(i)