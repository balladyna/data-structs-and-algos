# Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string with
# all punctuation removed. For example, if given the string "Let's try, Mike.", this function would return "Lets try
# Mike".
import re

user_input_message = "Write here something and I will remove punctuation: "


def remove_punctuation():
    user_input = input(user_input_message)
    user_input = re.sub(r'[^\w\s]', '', user_input)
    print(user_input)


remove_punctuation()
