id = input('Login :')

if id.lower() =='admin':  #입력받은 id를 소문자로 바꾸어서 'admin'인지 판단합니다.
    print('Hi, admin!')
    print('Please check log files.')
else:
    print('You are not admin.')    
