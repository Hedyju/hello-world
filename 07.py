# 무조건 첫 문자 하나를 맨 뒤로 보내고 그 뒤에 'ay'를 붙이는 프로그램

a = 'happy'; b = 'pig'; c = 'python'

new_a = a[1:] + a[0] + 'ay'
new_b = b[1:] + b[0] + 'ay'
new_c = c[1:] + c[0] + 'ay'

string = '{} -> {}'

print(string.format(a, new_a))
print(string.format(b, new_b))
print(string.format(c, new_c))
            
