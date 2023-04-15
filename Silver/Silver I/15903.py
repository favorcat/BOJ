import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, m = map(int,input().split())
card = list(map(int,input().split()))

cards = []
for a in card:
  heappush(cards, a)
  
for i in range(m):
  a = heappop(cards)
  b = heappop(cards)
  heappush(cards, a+b)
  heappush(cards, a+b)

print(sum(cards))