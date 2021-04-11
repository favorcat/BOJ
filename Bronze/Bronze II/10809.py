S = str(input())
al = [-1] * 26
for i in range(len(S)):
    if (al[ord(S[i])-97] == -1):
        al[ord(S[i])-97] = i
for k in range(26):
    print(al[k],end=' ')