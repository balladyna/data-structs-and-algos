# Write a Python program that outputs all possible strings formed by using the characters c , a , t , d , o ,
# and g exactly once.
import itertools
import random

characters_list = "catdog"
words_list = []


def generate_word(length):
    for subset in itertools.permutations(characters_list, length):
        words_list.append(('{}'*len(subset)).format(*subset))


for number in range(0,  len(characters_list) + 1):
    generate_word(number)
print(words_list)

