# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

alphabet = []

letter = "a"

for letters in range(0, 26):
    alphabet.append(letter)
    letter = chr(ord(letter) + 1)
print(alphabet)


