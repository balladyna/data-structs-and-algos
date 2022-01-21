# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

import random

different_values = "All values are different."
recurring_values = "In the list are recurring values."

list_a = [random.randrange(1, 30, 1) for sample_number_b in range(25)]
list_b = list(range(0, 20))

print(list_a)


def is_different(sample_list):
    if len(set(sample_list)) == len(sample_list):
        print(different_values)
    else:
        print(recurring_values)


is_different(list_a)
