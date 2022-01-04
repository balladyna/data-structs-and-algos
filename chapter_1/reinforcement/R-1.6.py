# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.
# Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.

prompt = ">>> "
square_message = "Choose number from 0 to 50:\n"
sum_message = "The sum of the squares of all the positive odd integers smaller than your number is: "
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value."


def adding_odd_squares():
    user_number_input = input(square_message + prompt)
    try:
        if 0 <= int(user_number_input) <= 50:
            sum_odd_squares = sum(square * square for square in (odd_number for odd_number in range(0, int(user_number_input)) if odd_number % 2 != 0))
            print(sum_odd_squares)
        else:
            print(wrong_value_message)
    except ValueError:
        print(ValueError)
        print(wrong_value_message)


adding_odd_squares()
