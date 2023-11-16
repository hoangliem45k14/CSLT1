print('Celsius(C)'.ljust(20) + 'Fahrenheit(F)')
print('________________________________')
for i in range(0,101,10):
    fahrenheit = 32 + 1.8 * i
    j=str(i)
    f=str(fahrenheit)
    print(j .ljust(20) + f)