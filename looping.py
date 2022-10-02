name = input("What's your name? ")
yes = "yes"
no = "no"

# TODO: Ask the user by name if they understand Python while loops
print("Dear {}, You should to know it is a loop" .format(name))
answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
while answer == 'yes':
    print("You are great! It is really simple, right?")
    answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
    if answer == 'no':
       print("Ok {}, no prob! The looping is a repetaing action" .format(name))
    answer = input("{}, now do you understand the looping of Python? \n(Enter yes/no)  " .format(name))
else: answer != yes or no
print("Please, add correct answer. Correct answer is: yes or no ")
# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.

  
# TODO: Outside the while loop, congratulate the user for understanding while loops