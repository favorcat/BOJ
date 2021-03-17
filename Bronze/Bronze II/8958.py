case = int(input())
for i in range(case):
    quiz = input()
    total = 0
    score = 0

    for k in range(len(quiz)):
        if k-1 >=0  :
            if quiz[k-1] == "O":
                if quiz[k] == "O":
                    score += 1
                else: score = 0
            else:
                if quiz[k] == "O":
                    score = 1
                else: score = 0
        else:
            if quiz[k] == "O":
                score = 1
            else: score = 0
        total += score

    print(total)
