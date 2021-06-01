#Building a Calculator
#First need 3 variables
num1= float(input("Please Enter Number One: "))
operator = input("Please Enter an Operator (+,-,*,/): ")
num2= float(input("Please Enter Number Two: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")

