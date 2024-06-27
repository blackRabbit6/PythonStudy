# 코딩 대회 개최
# 참석률 높이기 위한 이벤트 개최
# 댓글 작성자들중 1명 치킨, 3명 커피 줌

# 조건 1: 댓글 20개, 1~20이라 아이디 통일
# 조건 2: 댓글 내용과 상괍없이 무작위 추천,중복 불가
# 조건 3: random 모듈: suffle과 smaple 활용

# 예시
# --당첨자 발표--
# 치킨 : 1
# 커피: [2,3,4]
# --축하--

# 예제
# from random import *
# st = [1,2,3,4,5]
# print(st)
# shuffle(st) # shuffle 섞음
# print(st)
# print(sample(st,1)) # sample 그중 하나 뽑기

# 내가 쓴 답
# from random import *
#
# stu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(stu)
# chicken = sample(stu,1)[0] #sample이 리스트를 반환하므로 [0]을 사용해 단일 값으로 만듦
# stu.remove(chicken)
# # print(stu)
# coffee = sample(stu,3)
#
# print("--당첨자 발표--")
# print(f"치킨 : {chicken}")
# print(f"커피 : {coffee}")
# print("--축하--")

# 강사님 정답
from random import *

users = range(1,21) # 1~20까지 수 생성 range(1,20+1)
users = list(users) # users 형태 변형: range-list

print(users)
shuffle(users)
print(users)

winners = sample(users,4) # 4개수 출력, 1번째 치킨, 나머진 커피
print(winners)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨 : {0}".format(winners[0]))
print("커피 당첨 : {0}".format(winners[1:]))
print(" --    축하    -- ")