Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 세 시험 성적에 대한 평균 점수를 구하는 프로그램
>>> # 동시 할당을 이용해 여러 값을 한 번에 입력받는 방법을 사용한다.
>>> def main():
	print("This program computes the average of three exam scores.")
	score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
	average = (score1 + score2 + score3) / 3
	print("The average of the scores is:", average)

>>> 
