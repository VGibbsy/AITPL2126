def index(i):
    return 1 + (i >> 31) - (-i >> 31)
def check(n):
    # string array to store all kinds of number
    s = "negative", "zero", "positive"
    # function call to check the sign of number
    val = index(n)
    print(n, "is", s[val])
# test the above function
check(50)
check(-100)
check(0)

