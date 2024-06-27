# cabinet = {3:"유재석",100:"킴태호"}
# 출력
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

# 없을 때, 추가 하는법
# print(cabinet[5]) :에러 나고 코드 끝
# print(cabinet.get(5)) # 없으니 none 뜬 후 뒤 코드 작동
# print(cabinet.get(5, "Go")) # 이렇게 되면 cabinet이란 사전에 5번 키에 Go라는 value가 들어감
# print("hi")

# 확인법
# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-30"] = "지석진"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 만 출력
print(cabinet.keys())

# value 만 출력
print(cabinet.values())

# key,value 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)