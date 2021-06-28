'''
write a program to sum of three integers.However , if two values are equal sum will be zero.
'''
a=int(input('enter the first number'))
b=int(input('enter the second numbers'))
c=int(input('enter the third numbers'))
sum=0
if (a==b or b==c or a==c):
    print(' sum')
else:
    total=a+b+c
    sum=total
    print('the total',sum)
