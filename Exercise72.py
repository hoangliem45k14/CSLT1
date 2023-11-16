x=input('Nhap vao mot chuoi ky tu: ')
a=0
for i in range(0,len(x)//2):
    if x[i]!=x[len(x)-i-1]:
        a=1
        break
if a==1:
    print(x,'khong la chuoi palindrome')
else:
    print(x,'la chuoi palindrome')