prompt = ">>> "
square_message = "Choose number from 1 to 50:\n"
sum_message = "The sum of the squares of all the positive integers smaller than your number is: "
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value."


def adding_odd_squares():
    user_number_input = input(square_message + prompt)
    try:
        sum_odd_squares = sum(
            square * square for square in (odd_number for odd_number in range(1, int(user_number_input))
                                           if odd_number % 2 != 0))
        print(sum_odd_squares)
    except ValueError:
        print(ValueError)
        print(wrong_value_message)


adding_odd_squares()
