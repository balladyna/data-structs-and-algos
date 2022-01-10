# Write a short program that takes as input three integers, a, b, and c, from the console and determines if
# they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
prompt = ">>> "
user_input_message = "Choose three different numbers: "
sum_message = "Third number is a sum of first and second number"
difference_message = "First number is a difference of second and third number"
product_message = "Third number is a product of first and second number"
non_sum_message = "Third number is not a sum of first and second number"
non_difference_message = "First number is not a difference of second and third number"
non_product_message = "Third number is not a product of first and second number"
wrong_value_message = "Wrong value."


def is_correct():
    try:
        user_number_a = int(input(user_input_message))
        user_number_b = int(input(prompt))
        user_number_c = int(input(prompt))
        while True:
            if user_number_c == user_number_a + user_number_b:
                print(True)
                print(sum_message)
                if user_number_a == user_number_b - user_number_c:
                    print(True)
                    print(difference_message)
                    if user_number_c == user_number_a * user_number_b:
                        print(True)
                        print(product_message)
                        exit()
                    else:
                        print(False)
                        print(non_difference_message)
                        exit()
                else:
                    print(False)
                    print(non_difference_message)
                    if user_number_c == user_number_a * user_number_b:
                        print(True)
                        print(product_message)
                        exit()
                    else:
                        print(False)
                        print(non_product_message)
                        exit()
            else:
                print(False)
                print(non_sum_message)
                if user_number_a == user_number_b - user_number_c:
                    print(True)
                    print(difference_message)
                    if user_number_c == user_number_a * user_number_b:
                        print(True)
                        print(product_message)
                        exit()
                    else:
                        print(False)
                        print(non_product_message)
                        exit()
                else:
                    print(False)
                    print(non_sum_message)
                    if user_number_c == user_number_a * user_number_b:
                        print(True)
                        print(product_message)
                        exit()
                    else:
                        print(False)
                        print(non_product_message)
                        exit()
    except ValueError:
        print(wrong_value_message)


is_correct()
