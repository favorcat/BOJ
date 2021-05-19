n = int(input())
card = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))

result = {}
for key in card:
    if key in result:
        result[key] += 1
    else: result[key] = 1
    
print(' '.join(str(result[key]) if key in result else '0' for key in num))