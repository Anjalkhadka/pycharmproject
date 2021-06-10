'''A school decided to replace the desk in three classroom. Each desk site two student .
Each desk sit two student.
Give the number of student in each class, print the smallest possible numbers of desk that can be purchased.
'''
sectionA = int(input('enter the number of student in sectionA:'))
deskA = sectionA//2
remainA = sectionA%2
sectionB = int(input('enter the number of student in sectionB:' ))
deskB = sectionB//2
remainB = sectionB%2
sectionC = int(input('enter the number of student in sectionC:'))
deskC = sectionC//2
remainC = sectionC%2
print(f'the minimum number of required desks in class {deskA + deskB + deskC}')


