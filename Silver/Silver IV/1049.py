n, m = map(int,input().split())
packages = []	# 6개 패키지 가격을 담을 리스트
ones = []		# 낱개 가격을 담을 리스트

for i in range(m):
  # 6개 패키지, 낱개 가격을 입력
  package, one = map(int,input().split())
  
  # 패키지, 낱개 각 리스트에 추가
  packages.append(package)
  ones.append(one)

# 패키지, 낱개 가격 중 가장 낮은 가격을 뽑는다
mp = min(packages)
mo = min(ones)

# 끊어진 기타줄을 6으로 나누어 패키지로 살 갯수와 낱개로 살 갯수를 구한다
p = n//6
o = n%6

# 기타줄을 패키지+낱개로 살 가격 vs 모두 패키지로 살 가격 vs 모두 낱개로 살 가격
# 비교하여 가장 최솟값을 뽑는다
print(min(mp*p + mo*o, mp*(p+1), mo*n))
