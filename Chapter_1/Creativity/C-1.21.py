# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

user_message_one = "You will be asked to write something, when you type ctrl-D program will print what you write in " \
                   "reverse order."
user_message_two = "Write something: "


repeat = []

print(user_message_one)

while not False:
    try:
        user_input = input(user_message_two)
        repeat.append(user_input)
    except EOFError:
        print(EOFError)
        print(repeat[::-1])
        exit()

