x=-1
max=0
for i in range(1,101):
    n=int(input())
    if n>max:
        max=n
        x=x+1
print('The maximum value found was',max)
print('The maximum value was updated',x,'times')
    
        