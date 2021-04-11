s = input().upper()
a = list(set(s))
cnt = []
for i in a:
    cnt.append(s.count(i))
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    maxCnt = cnt.index(max(cnt))
    print(a[maxCnt])