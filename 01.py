Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n = 38724
>>> a = n // 10000
>>> n %= 10000
>>> b = n // 1000
>>> n %= 1000
>>> c = n // 100
>>> n %= 100
>>> d = n / 10
>>> e = n % 10
>>> print('만의 자리수:',a)
만의 자리수: 3
>>> print('천의 자리수:',b)
천의 자리수: 8
>>> print('백의 자리수:',c)
백의 자리수: 7
>>> print('십의 자리수:',d)
십의 자리수: 2.4
>>> print('일의 자리수:', e)
일의 자리수: 4
>>> 
