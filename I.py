'''
Given three integers, print the smallest one.(Three integers should be user input)
'''
a=int(input('enter the first number'))
b=int(input('enter the second number'))
c=int(input('enter the third number'))
if (a<b and a<c):
    print('the first number')
elif (b<a and b<c):
    print('the second number')
elif (c<a and c<b):
    print('the third number')
else:
    print('program end')
