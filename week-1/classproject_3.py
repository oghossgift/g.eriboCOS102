
PMT = float(input("Enter the regular payment amount: "))
R = float(input("Enter the annual interest rate (%): ")) 
n = int(input("Enter the number of times interest is compounded per year: "))
t = float(input("Enter the number of years: "))

R = R / 100

#  Annuity Formula
A = PMT * ((1 + R / n) ** (n * t) - 1) / (R / n)


print("Value of Annuity:", A)
