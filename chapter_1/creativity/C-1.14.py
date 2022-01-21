# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
import random

odd_message = "We have distinct pair of numbers in the sequence whose product is odd"
even_message = "All product of pair of numbers in the sequence are even"

list_a = [random.randrange(1, 50, 1) for sample_number in range(30)]

print(list_a)


def is_product_odd():
    for number, element in enumerate(list_a):
        if number + 1 < len(list_a) and number - 1 >= 0:
            first_el = list_a[number - 1]
            current_el = element
            if number < list_a[-1]:
                if first_el % 2 != 0:
                    if current_el % 2 != 0:
                        print(odd_message)
                        exit()
                    else:
                        continue
                else:
                    continue
    else:
        print(even_message)


is_product_odd()
