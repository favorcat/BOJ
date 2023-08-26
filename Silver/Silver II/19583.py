import sys
input = sys.stdin.readline
start, end, stream = map(str,input().split())
start = int(start[:2]+start[3:])
end = int(end[:2]+end[3:])
stream = int(stream[:2]+stream[3:])

student = set()
ans = 0
while True:
  try:
    time, name = input().split()
    time = int(time[:2]+time[3:])
    
    if time <= start:
      student.add(name)
    elif end <= time <= stream and name in student:
      student.remove(name)
      ans += 1
  except:
    break
print(ans)