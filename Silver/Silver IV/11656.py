s = input()
ans = [s[i:] for i in range(len(s))]
ans.sort()
print(*ans,sep="\n")