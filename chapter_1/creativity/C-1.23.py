# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be
# out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the
# following error message:
# “Don’t try buffer overflow attacks in Python!”
import random

user_message_one_message = "We will ask you for three numbers:"
user_number_one_message = "Please type number in range 0 - 10: "
user_number_two_message = "Please type number in range 10 - 20: "
user_number_three_message = "Please type number in range 0 - 50: "
error_message = "Don’t try buffer overflow attacks in Python!"
wrong_value_message = "Wrong value."

list_a = []

try:
    user_number_one = int(input(user_number_one_message))
    user_number_two = int(input(user_number_two_message))
    user_number_three = int(input(user_number_three_message))
    if 0 <= user_number_one <= 10 and 10 <= user_number_two <= 20 and 0 <= user_number_three <= 50:
        list_a = random.sample(range(user_number_one, user_number_two), 12)
        print(list_a[user_number_three - 1])
    else:
        print(wrong_value_message)
except IndexError:
    print(error_message)

