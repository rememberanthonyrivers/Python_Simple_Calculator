def calculate(num1, num2, op):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    print(f"{num1} {op} {num2} = {result}")


print("-------------------------------")
print("-------------------------------")
print("Welcome to my smart calculator!")
print("-------------------------------")
print("-------------------------------")

calculate(1, 2, "+")
calculate(3, 4, "-")
calculate(5, 5, "/")
calculate(50, 50, "*")
