
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
n = int(input("Enter Number of Times Interest is Compounded per Year: "))
T = float(input("Enter Time in Years: "))

# Convert rate to decimal
R = R / 100  

# Compound Interest Formula
A = P * (1 + R / n) ** (n * T)


print("Final Amount: ", A)
