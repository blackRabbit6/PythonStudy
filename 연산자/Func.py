# 숫자 관련 함수
print(abs(-5)) # abs - 절댓값               -> 5
print(pow(4, 2)) # pow - 앞숫자의 뒷숫자제곱  ->4**2= 16
print(max(5, 12)) # max - 입력된 수 중 최댓값  -> 12
print(min(5, 12)) # min - 입력된 수 중 최솟값  -> 5
print(round(3.14)) # round - 반올림          -> 3
print(round(4.99)) #                        -> 5

# 라이브러리 이용
from math import *
print(floor(4.99)) # floor(math 라이브러리 이용) - 내림 -> 4
print(ceil(3.14)) # ceil(math 라이브러리 이용) - 올림 -> 4
print(sqrt(16)) # sqrt(math 라이브러리 이용) - 제곱근 -> 4