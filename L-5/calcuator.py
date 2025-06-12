# simple calcuator using ladder statements

operator = input("Enter an Operator(+ , - , * , /)")

# perform for calculation

if operator == '+':
    num1 = float(input("Enter first Number : "))
    num2 = float(input("Enter second Number : "))
    result = num1 + num2
    print(f"sum of {num1} + {num2} = {result}")
elif operator == '*':
    num1 = float(input("Enter first Number : "))
    num2 = float(input("Enter second Number : "))
    result = num1 * num2
    print(f"sum of {num1} * {num2} = {result}")
else:
    print(f"This Operator not found")