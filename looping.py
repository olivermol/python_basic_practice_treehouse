name = input("What's your name? ")
YES_ANSWER = 'yes'
NO_ANSWER = 'no'

# TODO: Ask the user by name if they understand Python while loops
print("Dear {}, You should to know it is a loop" .format(name))
answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
while answer != YES_ANSWER:
    if answer == NO_ANSWER:
        print("Ok {}, no prob! The looping is a repetaing action" .format(name))
    answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
print("You are great! It is really simple, right {}?" .format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.

  
# TODO: Outside the while loop, congratulate the user for understanding while loops