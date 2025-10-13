name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# arithmetic operations or basic calculations\

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("what operation do you want to perform?")
operator = input("Enter operation (+, -, *, /): ")
if operator == '+':
    print(f"{x} + {y} = {x + y}")
elif operator == '-':
    print(f"{x} - {y} = {x - y}")
elif operator == '*':
    print(f"{x} * {y} = {x * y}")
elif operator == '/':
    try:
        print(f"{x} / {y} = {x / y}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")
    