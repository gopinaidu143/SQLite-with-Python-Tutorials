num = int(input('enter any positive number:'))
n= num
armnum = 0
while num>0:
    digit = num%10
    armnum += digit**3
    num //=10
if armnum==n:
    print('enterd number is armstrong number')
else:
    print('not a armstrong number')