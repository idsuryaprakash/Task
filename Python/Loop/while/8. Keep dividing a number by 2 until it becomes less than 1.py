#8. Keep dividing a number by 2 until it becomes less than 1
num = int(input("Enter a number: "))
count = 0

while num >= 1:
    num /= 2
    count += 1
print("Number of divisions:", count)