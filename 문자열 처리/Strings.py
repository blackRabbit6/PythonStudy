# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 문자열 변수명.lower() -> 전부 소문자로
print(python.upper()) # 문자열 변수명.upper() -> 전부 대문자로
print(python[0].isupper())
# 문자열 변수명[위치].isupper() -> 지정한 위치에 있는 단어가 대문자 이면 True, 아니라면 False
# 여기선 True
print(python[0].islower())
# 문자열 변수명[위치].islower() -> 지정한 위치에 있는 단어가 소문자 이면 True, 아니라면 False
# 여기선 False
print(len(python)) # len(문자열 변수명) -> 문자열 길이 출력
print(python.replace("Python", "Java"))
# 문자열 변수명.replace("?","??") ->문자열 안 ?를 ??로 바꿈

index = python.index("n") # 문자열 변수명.index("?") -> 문자열에서 ?가 몇번째 있는지 알려줌
print(index)
index = python.index("n", index+1) # 여기서는 아까 찾은 인덱스 부터 시작한다는 것임
print(index)

print(python.find("n")) # .find("?") -> ?가 앞에 쓰여진 문자열 변수에 어디에 있는지 출력
print(python.find("Java")) # 이러면 찾을 수 없어 -1 반환
# print(python.index("Java")) # python이란 변수에 문자 없어 걍 에러 뜨게 하고 종료 시킴

print(python.count("n")) # .count("?") -> 앞에 쓰인 문자열 변수에 가서 ?가 몇개인지 카운트함