fish = [int(input()) for _ in range(4)]
ans = 0
for i in range(3):
  if fish[i+1] > fish[i]:
    ans += 1
  elif fish[i+1] < fish[i]:
    ans -= 1

if len(set(fish)) == 1:
  print('Fish At Constant Depth')
elif ans == 3:
  print('Fish Rising')
elif ans == -3:
  print('Fish Diving')
else:
  print('No Fish')