#MINI CALCULATOR
print("MINI CALCULATOR")
while True:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    print("1. for addition")
    print("2. for substraction")
    print("3. for multiplication")
    print("4. for division")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("The sum of this number is:",a+b)
    elif choice == 2:
        print("The difference of this number is:",a-b)
    elif choice == 3:
        print("The product of this number:",a*b)
    elif choice == 4:
        if b == 0:
            print("Error: Division by zero is not allowed!")
        else:
            print("The quotient of this number:",a/b)
    else:
        print("invalid choice!!!")

    more = input("do you want to calculate more?")
    if more =="no":
        break
