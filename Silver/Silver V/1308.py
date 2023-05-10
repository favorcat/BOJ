import datetime
import sys
input = sys.stdin.readline

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
day = int(str(datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).split()[0])

cnt = 0
for i in range(1000):
  if i % 400 == 0:
    cnt += 366
  elif i % 100 == 0:
    cnt += 365
  elif i % 4 == 0:
    cnt += 366
  else:
    cnt += 365

if day >= cnt:
  print("gg")
else:
  print("D-"+str(day))