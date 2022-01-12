# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

min_max_message = "The smallest and largest numbers are:"

data = 2, 10, 4, 6, 8, 14, 88, 44, 33


def minmax(sample_list):
    min_number = sample_list[0]
    for small_number in sample_list:
        if small_number < min_number:
            min_number = small_number
    max_number = sample_list[0]
    for big_number in sample_list:
        if big_number > max_number:
            max_number = big_number
    min_max_tuple = min_number, max_number
    print(min_max_message)
    print(min_max_tuple)


minmax(data)
