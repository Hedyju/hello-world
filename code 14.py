subjects = {'toefl', 'toeic', 'gre', 'lsat'}

sub = input('Enter subject you want to register :')

if sub in subjects: # 입력받은 과목이 집합 subjects에 있는 경우
    print('You can register', sub, 'class.')
else:               # 입력받은 과목이 집합 subjects에 없는 경우 
    print('There is no', sub, 'class.')     