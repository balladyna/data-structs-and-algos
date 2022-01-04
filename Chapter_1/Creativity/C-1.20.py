# Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders
# the elements so that each possible order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints).
# Using only the randint function, implement your own version of the shuffle function.
import random, time

number_b_message = "Choose a number between 0 and 1000, it will be length and last number of your list: "
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value."

list_a = []

try:
    b = input(number_b_message)
    while len(list_a) <= int(b):
        if 0 <= int(b) <= 1000:
            list_a.append(random.randint(0, int(b)))
            if len(set(list_a)) == len(list_a):
                continue
            else:
                list_a.pop(-1)
        else:
            print(wrong_input_message)
    print(list_a)
except ValueError:
    print(ValueError)
    print(wrong_input_message)
