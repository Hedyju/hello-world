colors = ('blue','green','purple') #데이터가 3개 있는 튜플

color = input('What is your favorite color?') #색을 입력받기
if color.lower() in colors: #입력받은 색을 소문자로 바꾼 후에, colors에 있는 경우

    print('Oh!', color.title(), 'is also my favorite color.')

else:
    print(color.title(), 'is not my favorite color.')