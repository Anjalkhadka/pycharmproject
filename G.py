english=int(input('enter the marks of english'))
maths=int(input('enter the marks of maths'))
computer=int(input('enter the marks of computer'))
science=int(input('enter the marks of science'))
total=english+maths+computer+science
percentage=total/400*100
print('total marks=%2f' %total)
print('marks percentage=%2f'%percentage)
if percentage > 70:
    print('the number is distinction')
elif percentage > 60:
    print('the number is first division')
elif percentage > 40:
    print('the number is pass')
elif percentage < 40:
    print('the number is fail')
else:
    print('program end')