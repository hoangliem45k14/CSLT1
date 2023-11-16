n = int(input('Enter an integer (2 or greater): '))
print('The prime of factors of',n,'are:')
a = 2
if n < 2:
    print(n)
else:
    while a <= n:
        if n % a == 0:
            print(a)
            n /= a
        else:
            a += 1