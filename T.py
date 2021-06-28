'''
write a python function to find max three number.
'''
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter Third number: "))
def fun():
    if(num1>=num2) and (num1>=num3):
        i=num1


    elif(num2>=num1) and (num2>=num3):

         i=num2

    else:

         i=num3

    print("Largest number among  the three is",i)
fun()



