score = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0, '+':0.3, '-':-0.3, '0':0.0}
n = list(input())
print(sum(score[i] for i in n))
