a=int(input('Nhap so nhi phan: '))
d=0
m=1
while a>0:
        c=a%10
        d=d+(c*m)
        m=m*2
        a=int(a/10)
print('So thap phan la:',d)