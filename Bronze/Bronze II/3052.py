remain = set()
for i in range(10):
    n = int(input())
    remain.add(n%42)
print(len(remain))