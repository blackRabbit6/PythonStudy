# 코딩 스터디 함
# 월 4회 스터디 -> 3번 온라인 1번은 오프라인
# 조건1 랜덤 날짜
# 조건2 월별 날짜 다름이여서 28일 이내로 정함
# 조건3 매월 1~3은 스터디 준비로 재외함
# 출력: 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *
day = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + day + "일로 선정되었습니다.")
# 오류 이유 -> day는 int형이라 str로 변형해야 됨
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")
