'''
Check whether the user input number is even or odd and display it to user.
'''
num=int(input('enter the number'))
mod=num%2
if num>0:
    print('the number is odd')
else:
    print('the number is even')