import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    c, v = map(int,input().split())
    voter = []
    first = {}
    second = {}

    for _ in range(v):
        li = list(map(int,input().split()))
        voter.append(li)

        if li[0] in first:
            first[li[0]] += 1
        else: first[li[0]] = 1

    flag = False
    for key, value in first.items():
        if value > v//2:
            print(key, 1)
            flag = True
    if flag: continue

    sorted_first = sorted(first.items(), key=lambda x: x[1], reverse=True)
    for i in range(2):
        second[sorted_first[i][0]] = 0
    for s in voter:
        for favorite in s:
            if favorite == list(second.keys())[0] or favorite == list(second.keys())[1]:
                second[favorite] += 1
                break
    res = max(second.keys(), key=(lambda x: second[x]))
    print(res, 2)
