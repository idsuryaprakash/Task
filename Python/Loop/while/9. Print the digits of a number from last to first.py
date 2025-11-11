#9. Print the digits of a number from last to first
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10