n,k = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
ans = -1
def merge_sort(num_list, p, r):
  if p < r and cnt <= k:
    q = (p + r) // 2
    merge_sort(num_list, p, q)
    merge_sort(num_list, q + 1, r)
    merge(num_list, p, q, r)
    
def merge(a, p, q, r):
  i = p
  j = q + 1
  t = 1
  tmp = []
  global cnt, ans
  while i <= q and j <= r:
    if a[i] <= a[j]:
      tmp.append(a[i])
      i += 1
    else:
      tmp.append(a[j])
      j += 1
  while i <= q:
    tmp.append(a[i])
    i += 1
  while j <= r:
    tmp.append(a[j])
    j += 1
  i = p
  t = 0
  while i <= r:
    a[i] = tmp[t]
    cnt += 1
    if cnt == k:
      ans = a[i]
      break
    i += 1
    t += 1

merge_sort(a, 0, n-1)
print(ans)