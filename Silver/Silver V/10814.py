import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key = lambda x: int(x[0]))
for k in range(n):
    print(member[k][0], member[k][1])