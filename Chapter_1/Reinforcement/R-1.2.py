prompt = ">>> "
number_k_message = "Choose a number, we will check if it is even(True) or odd (False):\n"
even_message = "It's even number."
odd_number = "It's odd number."
wrong_input_message = "Wrong input."


def is_even():
    k = input(number_k_message + prompt)
    try:
        even_or_odd = divmod((int(k)), 2)
        if even_or_odd[-1] == 0:
            print(True)
            print(even_message)
        else:
            print(False)
            print(odd_number)
    except ValueError:
        print(ValueError)
        print(wrong_input_message)


is_even()
