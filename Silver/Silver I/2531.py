n, d, k, c = map(int,input().split())
rail = [int(input()) for _ in range(n)]

# 투포인터이므로 시작과 끝을 가리키는 포인터
start_point = 0
end_point = 0

# 먹을 초밥의 가짓수를 담을 딕셔너리
dic = {}
# 쿠폰 번호는 무조건 먹는다
dic[c] = 1

# 최대로 먹을 수 있는 초밥의 가짓수
ans = 0

# 처음에는 k 만큼 초밥을 먹어 끝 포인터를 이동시킨다.
while end_point < k:
  # 먹을 초밥이 딕셔너리에 없다면 생성해 준다
  if rail[end_point] not in dic:
    dic[rail[end_point]] = 1
  else: dic[rail[end_point]] += 1
  # 포인터 오른쪽으로 이동
  end_point += 1

# 시작(왼쪽) 포인터가 입력 받은 리스트의 가장 끝에 갈 때까지 반복
while start_point < n:
  # 이전의 ans와 새로 생성된 딕셔너리의 길이(먹은 초밥의 가짓수)를 비교해 더 큰 값을 넣어준다
  ans = max(ans, len(dic))
  
  # 옆(오른쪽)으로 이동하므로 시작 포인터가 가르키는 초밥 한개를 삭제
  dic[rail[start_point]] -= 1
  # 만약 삭제한 초밥이 0개가 된다면 딕셔너리에서 지운다
  if dic[rail[start_point]] == 0:
    del dic[rail[start_point]]
  
  # 만약 옆으로 이동한 끝 포인터가 가르키는 초밥을 딕셔너리에 추가
  # 리스트가 연결되어야 하기 때문에, 인덱스가 벗어나면 에러가 나므로
  # 인덱스에서 n만큼 나눈 나머지를 대입해 주어야 한다
  if rail[end_point%n] not in dic:
    dic[rail[end_point%n]] = 1
  else: dic[rail[end_point%n]] += 1
  
  # 포인터 오른쪽으로 이동
  start_point += 1
  end_point += 1

print(ans)
