fruits =['melon', 'strawberry', 'orange']  # 데이터가 3개 있는 리스트
f = input('Enter fruit :')  #과일 이름 입력받기
if f in fruits:   # 입력받은 과일이 리스트 fruits에 있는 경우
    print('I like', f)
else:            # 입력받은 과일이 리스트 fruits에 없는 경우
    print('I dont\'t like', f)