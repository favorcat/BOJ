import sys
input = sys.stdin.readline
T = int(input())
if T%10 != 0: print(-1)
else:
  li = [300,60,10]
  ans = [0,0,0]
  
  for i in range(3):
    ans[i] = T//li[i]
    T = T%li[i]

  for j in range(3):
    print(ans[j],end=" ")
