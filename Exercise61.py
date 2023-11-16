m=1
s=0
i=0
while m!=0:
    n=float(input('Enter your value:'))
    if n==0 and i<1:
        print('Error')
    s=s+n
    i=i+1
    m=n
print('The average of collection is',s/(i-1))