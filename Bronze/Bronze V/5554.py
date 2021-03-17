total = 0
for i in range(4):
    total += int(input())
minute = total // 60
sec = total - minute*60
print(minute)
print(sec)
