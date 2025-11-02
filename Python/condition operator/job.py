a=int(input('Enter your age '))
b=int(input('Enter your experience '))


if a>=18:
    print('you are eligible')
    if b>=2:
         print(' you are eligible')
         print('you are selected')
    else :
        print(a,'your age is up to  the mark,but you are not eligible')
else:
    print(a,'you are eligible')
