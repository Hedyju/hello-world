age = int(input('나이를 입력하세요 :'))

if age >= 65:  #나이가 65세 이상인경우
    print('입장료는 8000원 입니다')
elif 20 <= age < 65:  # 나이가 20세 이상이고 65세 미만인 경우
    print('입장료는 10000원 입니다')
elif 7 <= age < 20:  # 나이가 7세 이상이고 20세 미만인 경우
    print('입장료는 7000원 입니다')
else:    #나이가 7세 미만인 경우
    print('무료 입장입니다')

print('프로그램을 끝냅니다')