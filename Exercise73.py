x=input('Nhap vao day ki tu: ')
a=x
x=x.lower()
x=x.replace(' ','')
x=x.replace('.','')
for i in range(0,len(x)//2):
    if x[i]!=x[len(x)-i-1]:
        a=1
        break
if a==1:
    print(a,'khong la chuoi palindrome')
else:
    print(a,'la chuoi palindrome')

