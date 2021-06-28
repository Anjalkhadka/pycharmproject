'''
check whether the given year is leap year or not. If year is leap print 'LEAP YEAR' else 'COMMON YEAR'.
'''
year=int(input('enter the number of year'))
if year%4==0:
    print('leap year')
elif year%100==0:
    print('not leap year')
elif year%400==0:
    print('leap year')
else:
    print('not a leap year')



