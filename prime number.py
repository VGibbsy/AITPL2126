# Normally input will take as string so we need to give int(input()) so it takes has integer
num=int(input('Enter any number:'))
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print('{} is not a prime number'.format(num))
            break
    else:
        print('{} is a prime number'.format(num))
# if the entered number is less than or equal to 1 its not prime number
else:
    print('{} is not a prime number'.format(num))