x = 'Korea:Korean'
y = 'England:English'
z = 'France:French'

x2 = x.split(':') # 문자열 x를 ':'로 분리합니다 
print('in {}, people speak {}.'.format(x2[0], x2[1]))

y2 = y.partition(':') # ':'를 기준으로 문자열 y를 두 부분으로 분할합니다
print('in {}, people speak {}.'.format(y2[0], y2[2]))

index = z.index(':') # z에서 ':'의 위치 알려줌
print('in {}, people speak {}.'.format(z[:index], z[index+1:]))