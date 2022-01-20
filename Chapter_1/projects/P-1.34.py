# A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program
# that will write out the following sentence one hundred times: “I will never spam my friends again.” Your program
# should number each of the sentences and it should make eight different random-looking typos.


import string
import random


phrase = "I will never spam my friends again."


def generate_random():
    char1 = random.choice(string.ascii_lowercase)
    char2 = random.choice(string.ascii_lowercase)

    while char1 == char2:
        char2 = random.choice(string.ascii_lowercase)

    ran_pos1 = random.randint(0, len(phrase) - 1)
    ran_pos2 = random.randint(0, len(phrase) - 1)

    while ran_pos1 == ran_pos2:
        ran_pos2 = random.randint(0, len(phrase) - 1)

    orig_list = list(phrase)
    orig_list[ran_pos1] = char1
    orig_list[ran_pos2] = char2
    mod = ''.join(orig_list)
    print(mod)


g = 0


for number in range(0, 100):
    if g < 8:
        g = g
        if number >= 92 and g < 8:
            generate_random()
            g = g + 1
        else:
            a = random.randint(0, 1)
            if a == 0:
                print(phrase)
                continue
            elif a == 1:
                generate_random()
                g = g + 1
    elif g == 8:
        print(phrase)

