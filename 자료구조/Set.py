# 세트 -> 집합
#  중복 안됨, 순서 없음

my_set ={1,2,3,3,3}
print(my_set)

java = {"유","김","지"}
python = set(["유","하"])

#  교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 사용자 증가
python.add("김")
print(python)

# java 까먹음
java.remove("김")
print(java)