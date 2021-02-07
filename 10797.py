day = int(input())
car = list(map(int,input().split()))
warn = 0

for i in range (len(car)):
    if car[i] == day:
        warn += 1

print(warn)
