id = input('Login :') #아이디 입력받기

if id.lower() =='admin': #id를 소문자로 바꾸었을 때, 'admin'인 경우
    pwd = input('Password :')
    if pwd == '1234': #입력한 패스워드가 '1234'인 경우
        print('Welcome, admin')
    else:  # id는 'admin'이지만, 패스워드가 '1234'가 아닌 경우
        print('Wrong password')
else:   #id가 소문자로 바꾸었을 때, 'admin'이 아닌 경우
    print('You are not admin')        
    