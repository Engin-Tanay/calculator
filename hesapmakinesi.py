
#Hesap Makinesi#

a: float = 0.0
b: float = 0.0
result: float = 0.0

print("Enter the first number: ")
a = float(input())
print("Enter the second number: ")
b = float(input())

print("Enter the operation (+, -, *, /): ")
switch = input()
if switch == "+":
    result = a + b
elif switch == "-":
    result = a - b
elif switch == "*":
    result = a * b
elif switch == "/":
    if b != 0:
        result = a / b
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")

print("Result: ", result)