Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
    
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The amount in", years, "years is:", principal)

>>> 
