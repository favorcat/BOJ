today = list(map(int,input().split()))
Dday = list(map(int,input().split()))
mon = [31,28,31,30,31,30,31,31,30,31,30,31]

def calyear(year):
    rey = 0
    if year % 4 == 0: rey = 1
    if year % 100 == 0: rey = 0
    if year % 400 == 0: rey = 1
    
    return rey

def cal(year, month, day):
    r = 0
    for i in range(year):
        r += 365 + calyear(i)
    for i in range(month-1):
        if i == 1:
            r += calyear(year)
        r += mon[i]
    return r + day

if (Dday[0] - today[0] >= 1000 and cal(0, today[1], today[2]) <= cal(0, Dday[1], Dday[2])): print('gg')
else:
    print('D-{}'.format(cal(Dday[0], Dday[1], Dday[2]) - cal(today[0], today[1], today[2])))