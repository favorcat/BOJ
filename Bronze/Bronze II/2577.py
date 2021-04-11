A = int(input())
B = int(input())
C = int(input())
cal = str(A * B * C)
res = [0] * 10
for i in range(len(cal)):
    res[int(cal[i])] += 1
for k in range(10):
    print(res[k])