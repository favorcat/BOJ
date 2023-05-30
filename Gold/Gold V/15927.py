import sys
input = sys.stdin.readline
s = input().rstrip()
n = len(s)

def isPalindrome(arr, left, right):
  while left < right:
    if arr[left] != arr[right]: return 0
    left += 1
    right -= 1
  return 1

if not isPalindrome(s, 0, n-1):
  print(n)
elif not isPalindrome(s, 0, n-2):
  print(n-1)
else: print(-1)