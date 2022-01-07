# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.


user_message_one = "We will ask you for two numbers:"
user_number_one = int(input("Please type number in range 0 - 10: "))
user_number_two = int(input("Please type number in range 10 - 50: "))

array_a = []
array_b = []
array_c = []


def array_creator(sample_array):
    for number in range(user_number_one, user_number_two):
        sample_array.append(number)
    print(sample_array)


array_creator(array_a)

array_creator(array_b)


def array_mix():
    for number in range(0, user_number_two - user_number_one):
        number = array_a[number] * array_b[number] + array_a[number] * array_b[number]
        array_c.append(number)
    print(array_c)


array_mix()

