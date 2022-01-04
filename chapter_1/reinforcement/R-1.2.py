# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.


prompt = ">>> "
number_k_message = "Choose a number in range of -10000 to 10000, we will check if it is even(True) or odd (False):\n"
even_message = "It's even number."
odd_number = "It's odd number."
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value."


def is_even():
    k = input(number_k_message + prompt)
    try:
        if -10000 <= int(k) <= 10000:
            even_or_odd = divmod((int(k)), 2)
            if even_or_odd[-1] == 0:
                print(True)
                print(even_message)
            else:
                print(False)
                print(odd_number)
        else:
            print(wrong_value_message)
    except ValueError:
        print(ValueError)
        print(wrong_input_message)


is_even()
