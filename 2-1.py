Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # convert.py
>>> # 섭씨온도를 화씨온도로 변환하는 프로그램
>>> # 작성: 수전 컴퓨트웰
>>> def main():
	print("This program converts Celsius temperature to Fahrenheit.")
	print()
	celsius = eval(input("What is the Celsuius temperature? "))
	fahrenheit = 9/5 * celsius + 32
	print("The temperature is", fahrenheit, "degrees Fahrenhit.")
main()
