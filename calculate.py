import math
num1 = int(input("Enter a number: "))
option = input("Enter an option: ") 
num2 = int(input("Enter other number: "))

if option == "+":
    print(num1 + num2)
elif option == "-":
    print(num1 - num2)
elif option == "*":
    print(num1 * num2)
elif option == "/":
    print(num1 / num2)
elif option == "sqrt":
    print(math.sqrt(num1))
else: 
    print("Error")
