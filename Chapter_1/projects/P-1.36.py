# Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word
# appears in the list. You need not worry about efficiency at this point, however, as this topic is something that will
# be addressed later in this book.
from collections import Counter


user_message = "Write here something and I will count how many times each word appears, please do not use punctuation marks: "
user_input = input(user_message)


def count_word(sample_input):
    sample_input_list = sample_input.split(" ")
    print(Counter(sample_input_list))


count_word(user_input)
