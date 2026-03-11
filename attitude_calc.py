def calculator(a, b, op):
    if op == '+':
        print(f"Result = {a + b} 😎 Smart move bro!")
    elif op == '-':
        print(f"Result = {a - b} 🤔 Thoda soch le next time!")
    elif op == '*':
        print(f"Result = {a * b} 💪 Power move!")
    elif op == '/':
        print(f"Result = {a / b} 😅 Bas divide mat kar zero se!")
    else:
        print("😒 Bhai operator galat hai!")

print("😂 Welcome to Attitude Calculator 😂")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")
calculator(a, b, op)
