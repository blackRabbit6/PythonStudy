# 튜플: 리스트와 다르게 변경 불가, 속도가 리스트 보다 빠름

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

# menu.__add__("생선까지") : 에러( 튜플이기에 추가 못함)

(name,age,hobby) = ("김종국",20,"코딩")
print(name,age,hobby)