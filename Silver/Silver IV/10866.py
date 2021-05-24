import sys
s = []
n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().split()
    if (cmd[0] == 'push_front'):
        s.insert(0, cmd[1])
    elif (cmd[0] == 'push_back'):
        s.append(cmd[1])
    elif (cmd[0] == 'pop_front'):
        if (len(s) == 0):
            print(-1)
        else:
            print(s.pop(0))
    elif (cmd[0] == 'pop_back'):
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
    elif (cmd[0] == 'front'):
        if (len(s) == 0):
            print(-1)
        else: print(s[0])
    elif (cmd[0] == 'back'):
        if (len(s) == 0):
            print(-1)
        else: print(s[-1])