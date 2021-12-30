prompt = ">>> "
number_n_message = "Please choose a number:\n"
number_m_message = "Please choose a second number and we will check if it is a multiple (True) of the first number or " \
                   "not(False):\n"
wrong_input_message = "Wrong input."


def is_multiple():
    n = int(input(number_n_message + prompt))
    m = int(input(number_m_message + prompt))
    try:
        if n % m == 0:
            print(True)
        else:
            print(False)
    except ValueError:
        print(ValueError)
        print(wrong_input_message)


is_multiple()
