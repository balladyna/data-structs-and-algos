# The birthday paradox says that the probability that two people in a room will have the same birthday is more than
# half, provided n, the number of people in the room, is more than 23. This property is not really a paradox, but many
# people find it surprising. Design a Python program that can test this paradox by a series of experiments on randomly
# generated birthdays, which test this paradox for n = 5,10,15,20, . . . ,100.
from datetime import date, timedelta
import random
import calendar

birthday_list = []


def generate_birthday(sample_list):
    first_jan = date.today().replace(day=1, month=1)

    random_day = first_jan + timedelta(days=random.randint(0, 365 if calendar.isleap(first_jan.year) else 364))
    sample_list.append(random_day)


def is_duplicate(sample_list):
    if len(sample_list) == len(set(sample_list)):
        return False
    else:
        return True


n = 5


while n <= 100:
    n = n
    for number in range(0, n):
        generate_birthday(birthday_list)
        # print(birthday_list)
    test_group = is_duplicate(birthday_list)
    if test_group:
        print(str(n) + " " + "There are people with the same birthday")
        birthday_list.clear()
    else:
        print(str(n) + " " + "There are no duplicate of birthday")
        birthday_list.clear()
    n += 5
