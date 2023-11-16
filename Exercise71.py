num = int(input('Vui long nhap so bat ki: '))
doan = num/2
while doan**2-num>=10**-12:
    doan=(doan+num/doan)/2
print('Can bac hai cua so',num,'la:',doan)

