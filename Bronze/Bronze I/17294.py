import sys
input = sys.stdin.readline
k = list(map(int,input().rstrip()))
gap = 0
flag = 0

for i in range(1, len(k)):
  if i == 1:
    gap = k[i] - k[i-1]
  else:
    if k[i] - k[i-1] != gap:
      flag = 1
      break

if flag: print("흥칫뿡!! <(￣ ﹌ ￣)>")
else: print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")