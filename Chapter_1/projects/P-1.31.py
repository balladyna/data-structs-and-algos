# Write a Python program that can “make change.” Your program should take two numbers as input, one that is a
# monetary amount charged and the other that is a monetary amount given. It should then return the number of each kind
# of bill and coin to give back as change for the difference between the amount given and the amount charged.
# The values assigned to the bills and coins can be based on the monetary system of any current or former government.
# Try to design your program so that it returns as few bills and coins as possible.


list_of_bills_and_coins = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

charged_amount_message = "Write a charged monetary amount: "
given_amount_message = "Write a given monetary amount: "
wrong_value_message = "Given amount is to low, ask client for: "
wrong_input_message = "Wrong input."
return_message = "You should return to client: "


def make_change(sample_list):
    charged_amount_input = float(input(charged_amount_message))
    given_amount_input = float(input(given_amount_message))
    amount_to_return = round((given_amount_input - charged_amount_input), 2)
    list_of_return = []
    length_list = int(len(sample_list))
    if amount_to_return < 0:
        missing_value = charged_amount_input - given_amount_input
        print(wrong_value_message + str(missing_value))
    else:
        while amount_to_return > sum(list_of_return):
            for number, element in enumerate(sample_list):
                if (number + 1 <= length_list
                        and number - 1 >= 0):
                    first_el = sample_list[number - 1]
                    current_el = element
                    if amount_to_return == round((sum(list_of_return)), 2):
                        print(return_message + str(amount_to_return))
                        print({coins: list_of_return.count(coins) for coins in list_of_return})
                        return
                    else:
                        difference_of_return = round((amount_to_return - sum(list_of_return)), 2)
                        while first_el <= difference_of_return:
                            list_of_return.append(first_el)
                            difference_of_return = round((amount_to_return - sum(list_of_return)), 2)
                        if current_el <= difference_of_return:
                            list_of_return.append(current_el)
                        elif current_el > difference_of_return:
                            continue
        print(return_message + str(amount_to_return))
        print({coins: list_of_return.count(coins) for coins in list_of_return})
        return


try:
    make_change(list_of_bills_and_coins)
except ValueError:
    print(ValueError)
    print(wrong_input_message)
