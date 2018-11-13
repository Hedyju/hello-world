id = input('Login :')   #로그인 아이디를 입력받음.

if id =='admin':  #id가 admin인 경우
    print('Hi, admin!')
    print('Please check log files first.')
else:     #id가 admin이 아닌 경우
    print('Welcome!', id)    