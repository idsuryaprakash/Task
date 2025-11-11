#7. Compute the power of a number manually
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1

while exp > 0:
    result *= base
    exp -= 1
print("Power =", result)