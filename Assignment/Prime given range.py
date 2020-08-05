m = int(input('Enter lower range: '))
n = int(input('Enter upper range: '))

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
