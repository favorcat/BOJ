T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1,n+1)]
    for floor in range(k):
        for num in range(1, n):
            people[num] += people[num-1]
    print(people[-1])