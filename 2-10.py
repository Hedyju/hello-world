Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 킬로미터를 마일로 변환하는 프로그램
>>> def main():
	print("This program converts kilometers to miles.")
	print()
	kms = eval(input(Enter the distance in kilometers: "))
			 
SyntaxError: invalid syntax
>>> # 킬로미터를 마일로 변환하는 프로그램
def main():
	print("This program converts kilometers to miles.")
	print()
	kms = eval(input("Enter the distance in kilometers: "))
	miles = kms * 0.62
	print("The distance is", miles, "miles.")

			
>>> 
