# 변수

print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? : True")

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult =  age >= 3

print("우리집" + animal + "의 이름은 " + name +"이예요")
# hobby = "공놀이" -위에서는 산책이지만 여기서 초기화하여 변환함 -> 취미는 이제 공놀이로 변경되어 출력
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name ,"는 " , age, "살이며, ", hobby, "을 아주 좋아해요") ,는 +대신 사용가능하지만 기본적으로 띄어쓰기가 들어감
print(name+ "는 어른일까요? : " + str(is_adult))