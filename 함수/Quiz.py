# 표준 체중 프로그램
# 남자: 키(m) * 키 * 22
# 여자: 키(m) * 키 * 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
# 함수명 :std_weight
# 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 2째자리까지 표사

# 예시: 키 175cm 남자의 표준 체중은 67.38kg입니다.

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

gender = input("성별: ")
height = int(input("키: "))
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다".format(height, gender, weight))
