# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

list_a = [0, 2]
for number, element in enumerate(list_a):
    if number + 1 <= 9 and number - 1 >= 0:
        first_el = list_a[number - 1]
        current_el = element
        if number <= 9:
            list_a.append(((current_el - first_el) + (current_el + 2)))
print(list_a)
