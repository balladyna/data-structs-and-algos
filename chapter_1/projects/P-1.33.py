# Write a Python program that simulates a handheld calculator. Your program should process input from the Python console
# representing buttons that are “pushed,” and then output the contents of the screen after each operation is performed.
# Minimally, your calculator should be able to process the basic arithmetic operations and a reset/clear operation.

import math

c_number = 0
wrong_input_message = "Wrong input."
a_number_message = "Choose first number: "
b_number_message = "Choose second number: "
operation_message = """Choose mathematical operation:
    1 for +
    2 for -
    3 for *
    4 for /
    5 for ^
    6 for √: """

# def calculate():
while True:
    a_number_input = input(a_number_message)
    operation_input = input(operation_message)
    b_number_input = input(b_number_message)
    c_number = c_number + c_number
    if a_number_input.isnumeric() and operation_input.isnumeric() and b_number_input.isnumeric():
        if operation_input == "1":
            c_number = (float(a_number_input) + float(b_number_input))
        elif operation_input == "2":
            c_number = (float(a_number_input) - float(b_number_input))
        elif operation_input == "3":
            c_number = (float(a_number_input) * float(b_number_input))
        elif operation_input == "4":
            c_number = (float(a_number_input) / float(b_number_input))
        elif operation_input == "5":
            c_number = (pow(float(a_number_input), float(b_number_input)))
        elif operation_input == "6":
            c_number = float(a_number_input) ** (1 / float(b_number_input))
        print(c_number)
        c_number += c_number
        continue
    else:
        if a_number_input == "c" or operation_input == "c" or b_number_input == "c":
            break
        if a_number_input == "e" or operation_input == "e" or b_number_input == "e":
            exit()

