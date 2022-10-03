name = input("What's your name? ")
YES_ANSWER = 'yes'
NO_ANSWER = 'no'

print("Dear {}, You should to know it is a loop" .format(name))
answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
while answer != YES_ANSWER:
    if answer == NO_ANSWER:
        print("Ok {}, no prob! The looping is a repetaing action" .format(name))
    answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
print("You are great! It is really simple, right {}?" .format(name))