t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    queue = list(map(int,input().split()))
    check = [0 for i in range(len(queue))]
    check[m] = 1
    
    cnt = 0
    while True:
        if queue[0] == max(queue):
            cnt += 1
            if check[0] == 1:
                print(cnt)
                break
            else:
                check.pop(0)
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
            check.append(check.pop(0))
