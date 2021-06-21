n = int(input())
cnt = 0
for i in range(n):
    word = input()
    arr = []
    check = 0
    for k in range(len(word)):
        if word[k] not in arr:
            arr.append(word[k])
        else:
            if word[k] != arr[len(arr)-1]:
                check = 1
    if check == 0: cnt += 1
print(cnt)