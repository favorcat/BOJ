import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
if len(a) >= len(b): print('go')
else: print('no')