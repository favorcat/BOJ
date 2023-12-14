s = input()
if s.count(":-)") == 0 and s.count(":-(") == 0:
  print("none")
elif s.count(":-)") == s.count(":-("):
  print("unsure")
elif s.count(":-)") > s.count(":-("):
  print("happy")
else:
  print("sad")