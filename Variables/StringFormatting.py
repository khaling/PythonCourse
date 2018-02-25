age = 24
print('My age is ' + str(age) + ' years')
print('My age is {0} yaars'.format(age))
print('My name is {0} {1}'.format('Nar', 'Rai'))

print("""January: {2}
Febrauary: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {2}
October: {2}
November: {1}
December: {2}
""".format(28, 30, 31))

print('My age is %d years' %age)
print('my age is %d %s, %d %s'%(age, 'years', 6, 'months'))

for i in range(1, 12):
    print('No. %2d squared is %4d and cubed is %4d\n'%(i, i**2, i**3))
for i in range(1, 12):
    print('No. {0:2} squared is {1:<4} and cubed is {2:<4}'.format(i, i**2, i**3))

print("Pi is approximately %12.50f"%(22/7))
print("Pi is approximately {0:12.50}".format(22/7))

for i in range(1, 12):
    print('No. {:2} squared is {:4} and cubed is {:4}'.format(i, i**2, i**3))
