# Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one
# must repeatedly divide this number by 2 before getting a value less than 2.

user_input_message = "Write a number in range 2-1000: "
wrong_input_message = "Wrong input."
wrong_value_message = "Wrong value"
divide_message = f""

user_input = int(input(user_input_message))

list_a = []

try:
    if 2 <= user_input <= 1000:
        number: float = user_input / 2
        while True:
            if number >= 2:
                list_a.append(number)
            elif number < 2:
                list_a.append(number)
                print(f"We had to divide {len(list_a)} times to get a value which is less than 2")
                exit()
            number = number/2
    else:
        print(wrong_value_message)
except ValueError:
    print(ValueError)
    print(wrong_input_message)





