number1 = int(input('Write down the number please: '))
if number1 % 2 == 0 and number1 % 4 == 0:
    print(number1, 'is even and can be divided by 4.')
elif number1 % 2 == 0:
    print(number1, 'is even')
else:
    print(number1, 'is odd')
    
