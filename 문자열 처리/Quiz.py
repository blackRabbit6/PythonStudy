# 사이트 별로 비밀번호 만들어 주는 프로그램 작성
# ex: http://naver.com
# 1. http:// 제외 -> naver.com
# 2. 처음 만나는 점(.) 이후 부분 제외 => naver
# 3. 남은 글자 중 처음 3자리+글자 갯수+글자 내 'e' 갯수+"!" 로 구성
# nav51!

# site = "http://naver.com"
site ="http://youtube.com"
first = site.replace("http://", "")  # 1번
count = first[:first.index(".")]  # 2
pw = first[:3] + str(len(count)) + str(first.count("e")) + "!"
print("{0}의 생성된 비밀번호: {1}".format(site, pw))
