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
