a,b,v = map(int,input().split())
day = (v-b)/(a-b)
if (int(day) < day):
    print(int(day)+1)
else: print(int(day))