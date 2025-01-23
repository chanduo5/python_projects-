num1 = float(input("enter first no : "))
num2 = float(input("enter second no : "))
operation = input("enter (+,-,*,/): ")

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)
    
elif operation =="*":
    print(num1*num2)

elif operation == "/":
    if num2 != 0:
        print(num1/num2)

    else:
        print("error")