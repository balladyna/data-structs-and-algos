prompt = ">>> "
square_message = "Choose number from 1 to 50:\n"
sum_message = "The sum of the squares of all the positive integers smaller than your number is: "
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value."


def adding_squares():
    user_number_input = input(square_message + prompt)
    try:
        if 1 <= int(user_number_input) <= 50:
            total = sum(square * square for square in range(1, (int(user_number_input))))
            print(sum_message + str(total))
        elif int(user_number_input) == 0:
            print(ZeroDivisionError)
            print(wrong_value_message)
        else:
            print(wrong_value_message)
    except ValueError:
        print(ValueError)
        print(wrong_input_message)


adding_squares()
