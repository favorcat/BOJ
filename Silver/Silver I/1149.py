import sys
input = sys.stdin.readline

n = int(input())
house = [[0,0,0]]
for _ in range(n):
    house.append(list(map(int,input().split())))

for i in range(2, n+1):
  house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
  house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
  house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[n][0], house[n][1], house[n][2]))