s = list(map(ord,input()))
ans = []
for i in s:
  if 65 <= i <= 90: #대문자
    ans += chr(i+32)
  if 97 <= i <= 122: #소문자
    ans += chr(i-32)

print(''.join(ans))
