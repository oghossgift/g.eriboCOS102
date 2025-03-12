
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
T = float(input("Enter Time in Years: "))

# Compound Interest Formula
A = P * (1 + R / 100) ** T


print("Final Amount:", A)
