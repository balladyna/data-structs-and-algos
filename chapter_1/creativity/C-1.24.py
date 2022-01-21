# Write a short Python function that counts the number of vowels in a given character string.

user_input_message = "Write here something and I will count vowels: "
vowel_message = "The count of vowels is: "


def count_vowels():
    user_input: str = input(user_input_message)
    vowels = (user_input.count("i") + user_input.count("e") + user_input.count("a") +
              user_input.count("o"))
    print(vowel_message + str(vowels))


count_vowels()
