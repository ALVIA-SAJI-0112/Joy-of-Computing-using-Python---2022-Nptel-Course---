def fibanocci(n):
    if n<2:
        return n
    else:
        return fibanocci(n-1)+fibanocci(n-2)

n=int(input('Enter a non-negative number'))
if n<0:
    print('Fibanocci numbers are undefined for negative numbers')
else:
    print('Fibanocci number at position',n,'is',fibanocci(n))