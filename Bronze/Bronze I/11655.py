s = list(map(ord,input()))
ans = []
for i in s:
  if 65 <= i <= 90: #대문자
    if i+13 > 90: ans += chr(i+13-26)
    else: ans += chr(i+13)
  elif 97 <= i <= 122: #소문자
    if i+13 > 122: ans += chr(i+13-26)
    else: ans += chr(i+13)
  else: ans += chr(i)

print(''.join(ans))
