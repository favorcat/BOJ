import sys
input = sys.stdin.readline

s = input().rstrip()
tag = False
tmp = ""

for i in range(len(s)):
  if s[i] == "<":
    if i != 0: print(tmp[::-1], end="")
    tmp = "<"
    tag = True
  elif s[i] == ">":
    tmp += s[i]
    print(tmp, end="")
    tmp = ""
    tag = False
  else:
    if tag == False and s[i] == " ":
      print(tmp[::-1], end=" ")
      tmp = ""
    else:
      tmp += s[i]
  
  if i == len(s)-1:
    print(tmp[::-1], end="")