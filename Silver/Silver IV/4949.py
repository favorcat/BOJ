while True:
    s = input()
    if s == '.':
        break
    arr = []
    check = True
    for i in s:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] == '[':
                check = False
                break
            elif arr[-1] == '(':
                arr.pop()
        elif i == ']':
            if not arr or arr[-1] == '(':
                check = False
                break
            elif arr[-1] == '[':
                arr.pop()
    if check == True and not arr:
        print('yes')
    else:
        print('no')