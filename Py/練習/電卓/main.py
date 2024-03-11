import math
import settings as set
def calculator():
    first_number = float(input(set.sai))
    operation = input(set.tug)
    second_number = float(input(set.sag))

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    else:
        print("Invalid operation")
        return

    print(result)

calculator()