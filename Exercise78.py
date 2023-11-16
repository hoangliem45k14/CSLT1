n=int(input('Nhap vao mot so khong am: '))
kq=''
i=n
r=i%2
kq=str(r)+kq
i=i//2
while i>0:
    r=i%2
    kq=str(r)+kq
    i=i//2
print('So thap phan',n,'chuyen sang nhi phan la:',kq)