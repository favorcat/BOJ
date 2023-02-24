while(True):
  try :
    n = int(input())
  except : break
  k = ""
  while(True):
    k += "1"
    if int(k) % n == 0:
      print(len(k))
      break


while(True):
  try :
    n = int(input())
  except : break
  k = 0
  cnt = 1
  while(True):
    k = k * 10 + 1
    k = k % n
    if k == 0:
      print(cnt)
      break
    cnt += 1