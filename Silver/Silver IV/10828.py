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
            print(s.pop())
    elif (cmd[0] == 'size'):
        print(len(s))
    elif (cmd[0] == 'empty'):
        if (len(s) == 0):
            print(1)
        else: print(0)
    elif (cmd[0] == 'top'):
        if (len(s) == 0):
            print(-1)
        else: print(s[-1])