# MadLibs - Practice Input and Output
#
# Template:
#    I enjoy practice! I find it helps me to __(verb)__ better.
#    Without practice, my __(noun)__ would probably not even work.
#    My code is getting more __(adjective)__ every single day!


# Prompt the user for parts of speech and store them in variables
verb = input("Please add a verb "  )
noun = input("Please add a noun "  )
adjective = input("Please add an adjective "  )


# Output the template to the screen with the blanks filled out with what the user stated
print("I enjoy practice! I find it helps me to {} better. Without practice, my {} would probably not even work. My code is getting more {} every single day!" .format(verb, noun, adjective))