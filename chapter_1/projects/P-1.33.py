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

while True:
    while True:
        a_number_input = input(a_number_message)
        operation_input = input(operation_message)
        b_number_input = input(b_number_message)
        c_number += c_number
        if a_number_input.isnumeric() and operation_input.isnumeric() and b_number_input.isnumeric():
            match operation_input:
                case "1":
                    c_number = (float(a_number_input) + float(b_number_input))
                case "2":
                    c_number = (float(a_number_input) - float(b_number_input))
                case "3":
                    c_number = (float(a_number_input) * float(b_number_input))
                case "4":
                    c_number = (float(a_number_input) / float(b_number_input))
                case "5":
                    c_number = (pow(float(a_number_input), float(b_number_input)))
                case "6":
                    c_number = float(a_number_input) ** (1 / float(b_number_input))
            print(c_number)
            c_number += c_number
            continue
        else:
            match a_number_input:
                case "c":
                    break
                case "e":
                    exit()
            match operation_input:
                case "c":
                    break
                case "e":
                    exit()
            match b_number_input:
                case "c":
                    break
                case "e":
                    exit()

