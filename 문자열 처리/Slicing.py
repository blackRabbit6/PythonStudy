jumin = "901010-1234567"
# slice - 원하는 것만 출력할 수 있게 하는 법
print("성별: " + jumin[7])
print("출생년도: " + jumin[0:2]) # 0부터 2 직전까지 0~1
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6]) # 0부터 6 직전까지 0~5
print("뒤 7자리: " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터): " + jumin[-7:]) # 맨 뒤에서 부터 카운팅하고 -붙이기