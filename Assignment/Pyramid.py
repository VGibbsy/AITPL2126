n = 5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1  # decrementing k after every line
    for j in range(0, i + 1):
        if j % 2 == 1:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print("\n")