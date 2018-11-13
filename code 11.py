# 영문자 하나를 입력받아서 그 문자가 자음인지 모음인지를 판단하는 코드 #in 연산자 사용
vowels = 'aeiouAEIOU' #모음을 대소문자 모두 모아서 문자열로 만듭니다.

v = input('영문자를 하나 입력하세요 :')
if v in vowels:  #입력받은 문자가 vowels에 있는 문자인 경우
    print(v, '는 모음입니다')
else:            # 입력받은 문자가 vowels에 없는 문자인 경우
    print(v, '는 모음이 아닙니다')