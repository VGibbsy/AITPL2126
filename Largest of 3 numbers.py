# taking input from user
num1=input('Enter the first number: ')
# taking input from user
num2=input('Enter the second number: ')
# taking input from user
num3=input('Enter the third number: ')
# Comparing the given inputs
if (num1 >= num2) and (num1 >= num3) :
#storing the output in lnum
    lnum=num1
elif (num2 >=num1) and (num2 >=  num3) :
    lnum=num2
else:
    lnum=num3
print('The largest of {},{},{} given numbers is {}'.format(num1,num2,num3,lnum))
