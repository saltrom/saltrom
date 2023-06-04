num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
print("Please Select Action: '+'-'/'*'^^'")
operation = input()
result = 0
if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "/":
    result = num1 / num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "^^":
    result = num1 ** num2
    print(result)
else:
    break;
