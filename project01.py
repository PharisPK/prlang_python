# Sct211-0033/2022
# PHARIS KIRURI KARIUKI
# This is a calculator program
name=str(input("Please Enter Your Name: "))

print("Hello " + name)
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
Operation=input("Enter the operator(+,-,*,/): ")
if Operation=="+":
    print(x+y)
elif Operation=="-":
    print(x-y)
elif Operation=="*":
    print(x*y)
elif Operation=="/":
    print(x/y)
else:
    print("Wrong input")

