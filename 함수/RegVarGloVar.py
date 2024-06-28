# 지역변수와 전역변수
gun = 10

# def checkpoint(soldiers): # 경계근무
#     # gun = 20 # 지역변수
#     global gun # 전역변수, 밖에 있는 gun을 쓰겠다 라는 의미
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# 밑 코드처럼 반환값으로 해서 쓰는게 안전함
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
checkpoint_ret(gun,2)
print("남은 총: {0}".format(gun))