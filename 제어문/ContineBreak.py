absent = [2, 5] # 결석
no_book = [7] # 책 없음
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘은 여기까지.. {0}는 따라와...".format(student))
        break
    print("{0}, 책 읽어봐".format(student))