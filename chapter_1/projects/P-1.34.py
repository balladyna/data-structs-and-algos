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
    typo_sentence = ''.join(orig_list)
    print(typo_sentence)


typos_number = 0


for phrases_number in range(0, 100):
    if typos_number < 8:
        if phrases_number >= 92 and typos_number < 8:
            generate_random()
            typos_number = typos_number + 1
        else:
            randomized_phrase = random.randint(0, 1)
            if randomized_phrase == 0:
                print(phrase)
                continue
            elif randomized_phrase == 1:
                generate_random()
                typos_number = typos_number + 1
    elif typos_number == 8:
        print(phrase)

