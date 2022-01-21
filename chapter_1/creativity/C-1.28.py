# The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as
# v = p √vp1 +vp2+···+vpn .
# For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the
# vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of
# √42 +32 = √16+9 = √25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
import random, math

p_message = "Type number in range 0 - 10: "
wrong_value_message = "Wrong value."

p = int(input(p_message))
a = 0
b = 1
v = []
c = []

try:
    if 0 <= p <= 10:
        v = (random.sample(range(0, 20), p))
        print(v)
        for number in v:
            c.append(pow(number, p))
        print(c)
        print(math.sqrt(sum(c)))
    else:
        print(wrong_value_message)
except ValueError:
    print(wrong_value_message)
