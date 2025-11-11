#7.Calculate the sum of digits of a number using arithmetic only:
num = int(input("Enter a number:"))
sum= 0
for i in str(num):
    sum += int(i)
print("Sum of digits:",sum)   
