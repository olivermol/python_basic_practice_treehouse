name = input("Please enter your name: ")
number = input("Please enter a number: ")

number = int(number)
print("Hey {}! \nYour number is {}" .format(name, number))

fizz_number = number % 3 == 0
buzz_number = number % 5 == 0

if fizz_number and buzz_number:
   print("{} is a FizzBuzz number" .format(number))
elif fizz_number:
   print("{} is a Fizz number" .format(number))
elif buzz_number:
   print("{} is a Buzz Number" .format(number))
else:
   print("{} is neither a fizzy or a buzzy number")