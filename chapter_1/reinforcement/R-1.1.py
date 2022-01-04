# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.


prompt = ">>> "
number_n_message = "Please choose a number from range 0 to 10:\n"
number_m_message = "Please choose a second number from range 0 to 100 and we will check if the first number is a multiple (True) of this number number or not (False):\n"
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value."


def is_multiple():
    n = int(input(number_n_message + prompt))
    m = int(input(number_m_message + prompt))
    try:
        if 0 <= n <= 10 and 0 <= m <= 100:
            if m % n == 0:
                print(True)
            else:
                print(False)
        else:
            print(wrong_value_message)
    except ValueError:
        print(ValueError)
        print(wrong_input_message)


is_multiple()
