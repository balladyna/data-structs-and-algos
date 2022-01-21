# Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output
# device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be
# done on a separate line. After each such input, you should output to the Python console what would be displayed on
# your calculator.
import math

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


def calculate():
    a_number_input = float(input(a_number_message))
    operation_input = input(operation_message)
    b_number_input = float(input(b_number_message))
    c_number = 0
    match operation_input:
        case operation_input if operation_input == "1":
            c_number = float(a_number_input + b_number_input)
        case operation_input if operation_input == "2":
            c_number = float(a_number_input - b_number_input)
        case operation_input if operation_input == "3":
            c_number = float(a_number_input * b_number_input)
        case operation_input if operation_input == "4":
            c_number = float(a_number_input / b_number_input)
        case operation_input if operation_input == "5":
            c_number = float(pow(a_number_input, b_number_input))
        case operation_input if operation_input == "6":
            c_number = a_number_input ** (1 / b_number_input)
    print(c_number)


try:
    calculate()
except ValueError:
    print(wrong_input_message)
