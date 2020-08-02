a = int(input("Enter First Number :"))
b = int(input("Enter Second number:"))
print("Choose Options To Perform : ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter Your Choice :"))
if (choice==1) :
	print("Addition of A + B is : {} ".format(a+b))
elif (choice==2) :
	print("Subtraction of A - B is : {} ".format(a-b))
elif (choice==3) :
	print("Multiplication of A * B is : {} ".format(a*b))
elif (choice==4) :
	if(b == 0) :
		print("b cannot be 0(Zero) for Division operation")
	else :
		print("Division of A / B is : {} ".format(a/b))
else :
	print("Invalid Choice")