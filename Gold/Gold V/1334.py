n = input()
l = len(n)

if l == 1: # 1의자리 수
  n = int(n)
  if n == 9:
    print(11)
  else:
    print(n+1)

elif l & 1: # 홀수 자리 수
  a = int(n[:l//2][::-1]) # 앞자리
  b = int(n[l//2+1:]) # 뒷자리
  if a > b:
    print(n[:l//2]+n[l//2]+n[:l//2][::-1])
  else:
    if int(n[l//2]) == 9:
      c = str(int(n[:l//2])+1)
      if len(c) == len(n[:l//2]): print(c + "0" + c[::-1])
      elif len(c) > len(n[:l//2]): print(c + c[::-1])
    else:
      print(n[:l//2] + str(int(n[l//2]) + 1) + n[:l//2][::-1])

else: # 짝수 자리 수
  a = int(n[:l//2][::-1])
  b = int(n[l//2:])
  if a > b:
    print(n[:l//2]+n[:l//2][::-1])
  else:
    c = str(int(n[:l//2])+1)
    if len(c) == len(n[:l//2]):
      print(c + c[::-1])
    elif len(c) > len(n[:l//2]):
      print(c + c[::-1][1:])