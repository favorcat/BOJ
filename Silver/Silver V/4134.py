import math
n = int(input())

def is_prime_num(n):
    if n in [0, 1]:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(n):
    m = int(input())
    while True:
        if is_prime_num(m) == True:
            print(m)
            break
        else:
            m += 1