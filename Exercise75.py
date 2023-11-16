n=int(input("Nhap:"))
m=int(input('Nhap:'))
if n<m:
    c=n
    while n%c!=0 or m%c!=0:
        c-=1
else:
    c=m
    while n%c!=0 or m%c!=0:
        c-=1
print(c)