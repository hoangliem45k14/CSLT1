import random
s=''
x=False
k=0
n=0
def kt(s):
    if 'T T T' in s or 'H H H' in s:
        return True
    else:
        return False
for i in range(1,11):
    while x!=True:
        a=random.randint(1,2)
        k=k+1
        if a==1:
            s=s+'H '
            n=n+1
        else:
            s=s+'T '
            n=n+1
        x=kt(s)
    print(s+'('+str(n)+' flips)',end='\n')
    x=False
    s=''
    n=0    
print('On average,',k/10,'flips was needed.')       
    

        

        