a, b = map(int,input().split())
a_li = set(map(int,input().split()))
b_li = set(map(int,input().split()))
print(len(a_li - b_li) + len(b_li - a_li))