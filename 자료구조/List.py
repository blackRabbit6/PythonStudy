# # 리스트 [] -> 순서를 가지는 객체의 집합
#
# # 지하철 칸 별 - 10, 20, 30명
# sub1 = 10
# sub2 = 20
# sub3 = 30
#
# sub = [10, 20, 30]
# print(sub)
#
# sub = ["유재석","조세호","박명수"]
# print(sub)
#
# # 조세호는 어디에 위치?
# print(sub.index("조세호"))
#
# # 하하가 다음에 다음 칸에 탐
# sub.append("하하")
# print(sub)
#
# # 정형돈이 유재석과 조세호 사이 태움
# sub.insert(1,"정형돈")
# print(sub)
#
# # 지차철에 있는 사람들 중 뒤부터 한명씩 빼냄
# print(sub.pop())
# print(sub)
# # print(sub.pop())
# # print(sub)
# # print(sub.pop())
# # print(sub)
#
# # 같은 이름 사람 몇 명 있는지 확인
# sub.append("유재석")
# print(sub)
# print(sub.count("유재석"))

# # 정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# # 뒤집기
# num_list.reverse()
# print(num_list)
#
# # 모두 삭제
# num_list.clear()
# print(num_list)

#  다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)