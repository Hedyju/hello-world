Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 투자의 미래 가치를 계산하는 프로그램
>>> def main():

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The amount in", years, "years is:", principal)

    
>>> 
