import sys
s = []
n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().split()
    if (cmd[0] == 'push'):
        s.append(cmd[1])
    elif (cmd[0] == 'pop'):
        if (len(s) == 0):
            print(-1)
        else:
            print(s.pop(0))
    elif (cmd[0] == 'size'):
        print(len(s))
    elif (cmd[0] == 'empty'):
        if (len(s) == 0):
            print(1)
        else: print(0)
    elif (cmd[0] == 'front'):
        if (len(s) == 0):
            print(-1)
        else: print(s[0])
    elif (cmd[0] == 'back'):
        if (len(s) == 0):
            print(-1)
        else: print(s[-1])