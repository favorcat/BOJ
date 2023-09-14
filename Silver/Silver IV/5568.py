import itertools
import sys 
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().rstrip() for _ in range(n)]
print(len(set("".join(i) for i in itertools.permutations(cards, k))))