first_name = input('Enter your first name :')
last_name = input('Enter your last name :')
login_id = first_name[0].lower() + last_name.lower() #id 만들기
print('Welcome! your id is '", login_id "", sep=")
print()
print('=' * 32)
print('| Make a password as follows. |')
print('| - Must be at least 8 letter |')
print('| - Alphabet and numvers only |')
print('=' * 32)
print()
password = input('input new password :')  #패스워드를 입력받음.

if len(password) >= 8:  # 패스워드 길이가 8 이상인 경우
    if password.isalnum(): #isalnum()은 문자와 숫자로만 구성되었는지 판단함.
        print('Nice password')
    else:
        print('Alphabet and numbers only')
else:       #패스워드 길이가 8 미만인 경우
    print('Must be at least 8 letters')