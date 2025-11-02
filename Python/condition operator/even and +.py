a=int(input('Enter a number '))


if a>=1:
    print(a,'is positive number')
    if a%2==0:
         print(a,'is even number')
         print(a,'is a positive and even number')
    else :
        print(a,'is not a even number')
else:
    print(a,'is not possitive number')
