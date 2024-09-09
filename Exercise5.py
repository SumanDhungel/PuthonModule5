'''
#Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.
import random
num_dices = int(input("How many dices do you want to roll? "))
total_sum = 0
dice_faces = [1, 2, 3, 4, 5, 6]
for rolls in range(num_dices):
    roll = random.choice(dice_faces)
    total_sum += roll
print(f"The sum of the numbers of rolled dices is {total_sum}.")
'''

'''
#Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the
# reverse=True argument.
sorted_list = []
while True:
    user_input = input("enter a number or press enter to quit: ")
    if user_input == "":
        print("Program Terminated.")
        break
    try:
        number = float(user_input)
        sorted_list.append(number)
    except ValueError:
        print("Invalid input, Please enter a valid number.")
    sorted_list.sort(reverse=True)
    if len(sorted_list) > 5:
        sorted_list = sorted_list[:5]
if len(sorted_list) < 5:
    print("Entries not enough to display greatest five numbers.")
else:
    print("The five greatest numbers are:", sorted_list)
'''

'''
#Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the
# result is an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
import math

while True:
    number = input("Enter a number or press enter to quit: ")
    if number == "":
        print("Program Terminated.")
        break
    try:
        number = int(number)
    except ValueError:
        print("Invalid input, please enter a valid integer.")
        continue

    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
'''
'''
#Write a program that asks the user to enter the names of five cities one by one
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.
Cities = []
for i in range(5):
    city_name = input("Enter the name of any cities: ")
    if city_name == "":
        break
    else:
        Cities.append(city_name)
for city in Cities:
    print(city)
'''













