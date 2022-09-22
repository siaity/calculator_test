first_n = int(input("Enter first number: "))
second_n = int(input("Enter first number: "))
action = input("Select an action: +, -, *, /")


def calculate(first_n, second_n, action):
    if action == "+":
        return first_n + second_n
    elif action == "-":
        return first_n - second_n
    elif action == "*":
        return first_n * second_n
    elif action == "/":
        return first_n / second_n
    else:
        print("!!!_____Error_____!!! \n  You've done something wrong. Choose the correct action specified above!")


print(calculate(first_n, second_n, action))
