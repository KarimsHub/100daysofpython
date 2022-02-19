# # Day 1: Creating Band Name Generator
# print("Welcome to the Band Name Generator.")
# cityname = input("What's name of the city you grew up in? \n")
# petsname = input("What's your pet's name? \n")
# print("Your band name could be " + cityname + " " + petsname)

# # Day 2:
# BMI Calculator:
# height = input("What is your height in m? ")
# weight = input("What is your weight in kg? ")
# bmi =  float(weight) / (float(height)**2)
# bmi_rounded = round(bmi)
# print(bmi_rounded)

# # print(type(6 // 2))
# # // = always results an integer
# # score = score + 1 == score +=1

# # f -strings
# # score = 0
# # height = 1.8
# # isWinning = True
# # print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# # Your life in weeks program
# age = input("What is your current age? ")
# years_remaining = 90 - int(age)
# months = int(years_remaining) * 12
# weeks = int(years_remaining) * 52
# days = int(years_remaining) * 365

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# # Tip calculator
# print("Welcome to the tip calculator.")
# total_bill = float(input("What was the total bill? "))

# percentage_bill = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# split_in_people = int(input("How many people to split the bill? "))

# first_result = ((total_bill / split_in_people) / 100) * percentage_bill
# second_result = ((total_bill / split_in_people) + first_result)
# rounded_second_result = round(second_result, 2)

# print(f"Each person should pay: €{rounded_second_result}")

# # Day 3:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("What are your age? "))

#     if age < 12:
#         bill = 5
#         print("child tickets are 5€")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are 7€")
#     else:
#         bill = 12
#         print("Adult tickets are 12€")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         # Add 3€
#         bill += 3
    
#     print(f"Your final bill is {bill}")


# else:
#     print("you can't ride the rollercoaster!")

# # BMI Calculator 2.0:

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = weight / (height ** 2)
# bmi_rounded = round(bmi)

# if bmi_rounded < 18.5:
#     print(f"Your BMI is {bmi_rounded}, you are underweight")
# elif bmi_rounded < 25:
#     print(f"Your BMI is {bmi_rounded}, you are normal weight")
# elif bmi_rounded < 30:
#     print(f"Your BMI is {bmi_rounded}, you are slightly overweight")
# elif bmi_rounded < 35:
#     print(f"Your BMI is {bmi_rounded}, you are obese")
# else:
#     print(f"Your BMI is {bmi_rounded}, you are clinically obese")

# # Leap Year Program
# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         print("This year is not a Leap year")
#     else:
#         print("This year is a Leap year")    
# else:
#     print("This year is not a leap year")

# # Pizza Order Program
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M, or L? ")
# add_pepperoni = input("Do you want pepperoni? Y or N? ")
# extra_cheese = input("Do you want some extra cheese? Y or N? ")
# bill = 0

# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"Your final bill is: {bill}")
#         else:
#            print(f"Your final bill is: {bill}") 
#     else:
#         print(f"Your final bill is: {bill}")
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"Your final bill is: {bill}")
#         else:
#            print(f"Your final bill is: {bill}") 
#     else:
#         print(f"Your final bill is: {bill}")
# elif size == "L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"Your final bill is: {bill}")
#         else:
#            print(f"Your final bill is: {bill}") 
#     else:
#         print(f"Your final bill is: {bill}")
# else:
#     print("Please try again")

# # Love Calculator Program
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# love_score = 0

# name1_lower_case = name1.lower()
# name2_lower_case = name2.lower()
# number_of_t = name1_lower_case.count("t") + name2_lower_case.count("t")
# number_of_r = name1_lower_case.count("r") + name2_lower_case.count("r")
# number_of_u = name1_lower_case.count("u") + name2_lower_case.count("u")
# number_of_e = name1_lower_case.count("e") + name2_lower_case.count("e")
# true_score = number_of_t + number_of_r + number_of_u + number_of_e

# number_of_l = name1_lower_case.count("l") + name2_lower_case.count("l")
# number_of_o = name1_lower_case.count("o") + name2_lower_case.count("o")
# number_of_v = name1_lower_case.count("v") + name2_lower_case.count("v")
# love_score = number_of_l + number_of_o + number_of_v + number_of_e
# new_score = str(true_score) + str(love_score)

# if int(new_score) < 10 or int(new_score) > 90:
#     print(f"Your score is {new_score}, you go together like coke and mentos")
# elif int(new_score) >= 40 and int(new_score) <= 50:
#     print(f"Your score is {new_score}, you are alright together")
# else:
#     print(f"Your score is {new_score}")

# # Alice in Wonderland Adventure
# print('''                   .'\   /`.
#                  .'.-.`-'.-.`.
#             ..._:   .-. .-.   :_...
#           .'    '-.(o ) (o ).-'    `.
#          :  _    _ _`~(_)~`_ _    _  :
#         :  /:   ' .-=_   _=-. `   ;\  :
#         :   :|-.._  '     `  _..-|:   :
#          :   `:| |`:-:-.-:-:'| |:'   :
#           `.   `.| | | | | | |.'   .'
#             `.   `-:_| | |_:-'   .'
#          jgs  `-._   ````    _.-'
#                   ``-------''
#                   ''')
# print("Welcome to the Alice in Wonderland Adventure")
# print("Your mission is to escape the Wonderland and resque the helpless Bunny from the Emperor! \nAfter a few minutes of walking you meet a soldier who ask's about your ID")

# first_answer = input("Do you want to discuss that you don't have an ID or do you want try to escape with running? Please type \"discuss\" or \"escape\"!: ").lower()
# if first_answer == "discuss":
#     print("The soldier does not accept the answer and take`s you to the emperor's castle")
#     second_answer = input("In the castle you've been locked in a cell with the bunny right next to you. \nYou two are talking for quite a while and the bunny suggests you to overwhelm the guard protecting the cell. \nDo you want to overwhelm or wait for sunrise? Please type \"overwhelm\"or \"wait\"!: ").lower()
#     if second_answer == "overwhelm":
#         print("You've successfully overwhelmed the guard and escaped the cell with the bunny")
#     elif second_answer == "wait":
#         print("Game over: Waiting didn't helped you by finding a solution. The bunny died!")
#     else:
#         print("Game over: You didn't choose one of the given answers!")
# elif first_answer == "escape":
#     print("Game over: You couldn't escape the soldier and died. Please try again")
# else:
#     print("Game over: You didn't choose one of the given answers!")

# # Day 4

# # Heads or Tails program
# import random

# random_number = random.randint(0, 1)
# if random_number == 0:
#     print("Tails")
# else:
#     print("Heads")

# # Banker Roulette program
# import random

# names_string = input("Give me everybody's names, seperated by a comma: ")
# names = names_string.split(", ")
# #number_of_names = (len(names) -1)
# random_number = random.randint(0, (len(names) -1))
# print(f"{names[random_number]} is going to buy the meal today!")

# # nested list
# # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# # dirty_dozen = [fruits, vegetables]

# # Treasure Map Program
# row1 = ["😉","😉","😉"]
# row2 = ["😉","😉","😉"]
# row3 = ["😉","😉","😉"]

# map = [row1, row2, row3]
# position = input("Where do you want to put the treasure? ")
# column_number = (position[0])
# row_number = (position[1])

# map[int(row_number) -1][int(column_number) -1] = "x"
# print(f"{row1}\n{row2}\n{row3}")

# # Rock paper scissors game Program

# import random
# # Rock
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# # Paper
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# # Scissors
# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# computer_choice = random.randint(0,2)
# # rock wins against scissors
# # scissors win against paper
# # paper wins against rock
# if your_choice == 0:
#     print(rock)
#     if computer_choice == 2:
#         print(f"Computer chose:\n {scissors}\nYou win!")
#     elif computer_choice == 0:
#         print(f"Computer chose:\n {rock}\nDraw!")
#     else:
#         print(f"Computer chose:\n {paper}\nYou lose!")
# elif your_choice == 1:
#     print(paper)
#     if computer_choice == 0:
#         print(f"Computer chose:\n {rock}\nYou win!")
#     elif computer_choice == 1:
#         print(f"Computer chose:\n {paper}\nDraw!")
#     else:
#         print(f"Computer chose:\n {scissors}\nYou lose!")
# elif your_choice == 2:
#     print(scissors)
#     if computer_choice == 1:
#         print(f"Computer chose:\n {paper}\nYou win!")
#     elif computer_choice == 2:
#         print(f"Computer chose:\n {scissors}\nDraw!")
#     else:
#         print(f"Computer chose:\n {rock}\nYou lose!")
# else:
#     print("Please input the right number")

# # Day 5

# # Average Height program
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# number_of_students = 0
# overall_height = 0
# for height in student_heights:
#     overall_height += height
#     number_of_students += 1
# average = overall_height / number_of_students
# rounded_average = round(average)
# print(f"The average is {rounded_average}")

# # Highest Score program
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

# # min() and max() Functions are the easy way

# # For Loop with Range
# for number in range(1, 10): # going from 1 - 9 (not including 10)
#     print(number)

# # Adding Events:

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# # FizzBuzz program
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# # Project Password Generator
# import random
# from typing import final

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# lenght = int(input("How many letters would you like in your password?\n"))
# nr_numbers = int(input("How many numbers would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like in your password?\n"))



# # easy way

# password = ""

# for letter in range(0, lenght):
#     random_letter = random.choice(letters)
#     password += random_letter
# for letter in range(0, nr_symbols):
#     random_numbers = random.choice(numbers)
#     password += random_numbers
# for letter in range(0, nr_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol

# print(password)

# # hard way with more randomization

# password_list = []

# for letter in range(0, lenght):
#     random_letter = random.choice(letters)
#     password_list.append(random_letter)
# for letter in range(0, nr_symbols):
#     random_numbers = random.choice(numbers)
#     password_list.append(random_numbers)
# for letter in range(0, nr_symbols):
#     random_symbol = random.choice(symbols)
#     password_list.append(random_symbol)

# random.shuffle(password_list) #shuffling the items in the list

# print(password_list)

# # changing the list into string
# final_pw = ""
# for char in password_list:
#     final_pw += char
# print(final_pw)


# # Day 6

# # Reeborgs World Hordle 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_round():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for round in range(0,6):
#     one_round()

# # Reeborgs World Hordle 2
# while not at_goal():
#     one_round()

# # Reeborgs World Hordle 3
# while not at_goal():
#     if wall_in_front(): #removed move() from one_round() function
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#     elif front_is_clear():
#         move()

# # Reeborgs World Hordle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_round():
#     turn_left()
#     while wall_on_right():
#         move()
  
#     turn_right()
#     move()
#     turn_right()
    
#     while front_is_clear():
#         move()
#     turn_left()
        
# while not at_goal():
#     if wall_in_front():
#         one_round()
#     else: 
#         move()

# # Reeborgs World Maze
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# # Day 7

# # hangman program

# import random
# import hangmanart
# import hangmanwords


# print(hangmanart.logo)
# chosen_word = random.choice(hangmanwords.word_list)
# word_lenght = len(chosen_word)
# display = []

# running = True
# for char in chosen_word:
#     display += "_"
# print(f"{' '.join(display)}")

# lives = 6
# letter_list = []

# while running:
#     # print(f"Psst , the solution is {chosen_word}") # for debugging purpose


#     guess = input("Guess a letter: ").lower()
#     if guess in letter_list:
#         print("You've already guessed that letter")
#     else:
#         letter_list.append(guess)
#         for position in range(word_lenght):
#             letter = chosen_word[position]
#             if letter == guess:
#                 display[position] = letter

#         if guess not in chosen_word:
#             lives -= 1
#             print(f"You guessed letter {guess}, that's not in the word. You lose a life.")
#             print(hangmanart.stages[lives])  
#             if lives == 0:
#                 running = False
#                 print("You lose!")
#         print(f"{' '.join(display)}")

#         if not "_" in display:
#             print("You won!")
#             running = False

# # Day 8

# #function that allows for input

# def greet(name):
#     print(f"Hello {name}.")
# greet("Karim")


# #functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# #greet_with("Karim", "Barcelona")

# greet_with(name = "Karim", location = "Barcelona")


# # Area calculation program
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))

# def area_calc(height, width, coverage=5):
#     number_of_cans = (height * width) / coverage
#     print(round(number_of_cans))

# area_calc(height=test_h,width=test_w)

# # prime number program
# n = int(input("Check this number: "))

# def prime_checker(number):
#     is_prime = True
#     for num in range(2, number):
#         if number % num == 0:
#             is_prime = False
#     if is_prime:
#         print(f"The number {number} is a prime number")
#     else:
#         print(f"The number {number} is not a prime number")


# prime_checker(number=n)



# # Ceasar cipher program

# import hangmanwords
# import art

# alphabet = hangmanwords.alphabet

# def encrypt(plain_text, shift_amount):
#     encoded_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         calc_index = index + shift
#         if calc_index > 25:
#             oversize = calc_index - 25
#             new_letter = alphabet[oversize -1]
#             encoded_word += new_letter
#         else:
#             new_letter = alphabet[calc_index]
#             encoded_word += new_letter
#     print(f"The encoded_word is {encoded_word}")

# encrypt(plain_text=text, shift_amount=shift)

# def decrypt(plain_text, shift_amount):
#     decoded_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         calc_index = index - shift
#         # if calc_index < 0:
#         #     oversize = calc_index - 25
#         #     new_letter = alphabet[oversize -1]
#         #     decoded_word += new_letter
#         new_letter = alphabet[calc_index]
#         decoded_word += new_letter
#     print(f"The decoded_word is {decoded_word}")

# decrypt(plain_text=text, shift_amount=shift)

# def ceasar(direction, plaintext, shift_amount):
#     encoded_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         if direction == "encode":  #for encryption the following code:
#             calc_index = index + shift
#             if calc_index > 25:
#                 oversize = calc_index - 25
#                 new_letter = alphabet[oversize -1]
#                 encoded_word += new_letter
#             else:
#                 new_letter = alphabet[calc_index]
#                 encoded_word += new_letter
#         elif direction == "decode":
#             calc_index = index - shift
#             new_letter = alphabet[calc_index]
#             encoded_word += new_letter          
#         else:
#             print("Please type in 'encode or 'decode!")
#     print(f"The word is {encoded_word}")

# print(art.logo)
# running = True

# while running:
#     direction = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n")
#     text = input("Type in your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     ceasar(direction, plaintext=text, shift_amount=shift)

#     question = input("You want to run again? Press 'yes or 'no'.\n")
#     if question == "no":
#         running = False

# # Day 9

# #Dictionaries

# programming_dictionary = {
#     "Bug": "an error", 
#     "Function": "a piece of code",
#     "Loop": "the action of doing something over and over again",  
# }

# #Retrieving items from dictionary
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])
# print(programming_dictionary["Loop"])

# #Adding new items to dictionary 
# programming_dictionary["Hello"] = "Definition for sth"
# print(programming_dictionary)

# #create an empty dictionary
# empty_dictionary = {}

# #wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "new problem in your computer"
# print(programming_dictionary)

# #Loop through a dictionary
# for key in programming_dictionary:
#     print(key) #getting the key
#     print(programming_dictionary[key]) # getting the value of the looped key

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}
# for key in student_scores:
#     number = student_scores[key]
#     if number >=91:
#         value = "Outstanding"
#         student_grades[key] = value
#     elif number >=81:
#         value = "Exceeds Expectations"
#         student_grades[key] = value
#     elif number >=71:
#         value = "Acceptable"
#         student_grades[key] = value
#     else:
#         value = "Fail"
#         student_grades[key] = value

# print(student_grades)

# nexting dictionaries into dictionary
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited": ["Freiburg", "Hamburg", "Berlin"],
#         "total_visits": 3
#     },
# }

# print(travel_log["France"])
# print(travel_log["Germany"])

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Freiburg", "Hamburg", "Berlin"],
#         "total_visits": 3,
#     },
# ]


# def add_new_country(country, total_visits, cities_visited):
#     travel_log.append({"country": country, "cities_visited": cities_visited, "total_visits": total_visits})

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# print(travel_log)



# # Secret Auction program

# import art

# print(art.logo1)
# print("Welcome to the secret auction program")
# bids = {}
# running = True



# def calc_winner(bids):
#     highest_bid = 0
#     winner_name = ""
#     for bid in bids:
#         if bids[bid] > highest_bid:
#             highest_bid = bids[bid]
#             winner_name = bid
#     print(f"The winner is {winner_name} with a bid of {highest_bid}")

# while running:
#     name = input("What is your name? ")
#     bid = int(input("What is you bid? "))

#     bids[name] = bid
    
#     more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
#     #clear = print("\n" * 100)
#     if more_bidders == "no":
#         print(bids)
#         #calc_winner(bids)
#         running = False
#         calc_winner(bids)
        
# Day 10

# Functions with outputs

# f_name = input("Whats your first name? ")
# l_name = input("Whats your first name? ")

# def format_name(f_name, l_name):
#     formated_name1 = f_name.title()
#     formated_name2 = l_name.title()
#     return f"{formated_name1} {formated_name2}" #return is the end of a function

# formated string = format_name(f_name, l_name)

# # Days in month programn

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return False
#         else:
#             return True   
#     else:
#         return False

# def days_in_month(year, month):
#     """ Take the year and month as input and return number of days the month has"""
#     if month > 12 or month < 1:
#         return "Invalid month"
#     leap_year = is_leap(year)
#     if leap_year:
#         month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
#         return month_days[month -1]
#     else:
#         month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#         return month_days[month -1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# # Calculator program

# import art

# #Add function
# def add(first_number,next_number):
#     return first_number + next_number


# #subtract function
# def subtract(first_number,next_number):
#     return first_number - next_number


# #multiply function
# def multiply(first_number,next_number):
#     return first_number * next_number


# #divide function
# def divide(first_number,next_number):
#     return first_number / next_number

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }


# def calculator():
#     print(art.logo2)

#     running = True

#     first_number = float(input("Whats the first number?: "))
#     for key in operations:
#         print(key)

#     while running:
#         pick_operator = input("Pick an operation: ")
#         next_number = float(input("What's the next number?: "))

#         function = operations[pick_operator]
#         first_answer = function(first_number, next_number)

#         print(f"{first_number} {pick_operator} {next_number} = {first_answer}")

#         repeat = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ")
#         if repeat == "n":
#             running = False
#             calculator()
#         else:
#             first_number = first_answer

# calculator()

# # Day 11

# #Blackjack program

# #imports:
# import art
# import random

# # functions:
# def deal_card_for_you():
#     your_hand.append(random.choice(cards))

# def deal_card_for_computer():
#     computers_hand.append(random.choice(cards))


# def calc_your_score(hand):
#     return sum(hand)

# def calc_winner(user_score, enemy_score):
#     if user_score > 21:
#         print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#         print("You went over. You lose!")
#     elif user_score <= 21 and user_score > enemy_score:
#         deal_card_for_computer()
#         enemy_score = calc_your_score(hand=computers_hand)
#         print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#         if enemy_score > user_score and enemy_score < 21:
#             print("You lose!")
#         elif user_score == enemy_score:
#             print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#             print("It's a draw!")
#         else:
#             print("You won!")
#     elif enemy_score > 21:
#         print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#         print("Computer went over. You won!")
#     elif user_score > enemy_score:
#         print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#         print("You won!")
#     elif user_score < enemy_score:
#         print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#         print("You lose!")
#     elif user_score == enemy_score:
#         print(f"Your final hand: {your_hand}, final score: {user_score}\nComputer's final hand: {computers_hand}, final score: {enemy_score}")
#         print("It's a draw!")

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# your_hand = []
# computers_hand = []

# def blackjack():
#     running = True
#     print(art.logo3)
    
#     while running:
            
#         game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

#         if game == "y":
#             for i in range(2):
#                 deal_card_for_you()
#             deal_card_for_computer()
#             user_score = calc_your_score(hand=your_hand)
#             enemy_score = calc_your_score(hand=computers_hand)
#             print(f"Your cards: {your_hand}, current score {user_score}\nComputer's first card: {computers_hand[0]}")
#             another_card = input("Type 'y' to get another card or 'n' to pass: ")
#             if another_card == "y":
#                 deal_card_for_you()
#                 user_score = calc_your_score(hand=your_hand)
#                 print(f"Your cards: {your_hand}, current score {user_score}\nComputer's first card: {computers_hand[0]}")
#                 deal_card_for_computer()
#                 enemy_score = calc_your_score(hand=computers_hand)
#                 calc_winner(user_score, enemy_score)
#             else:
#                 deal_card_for_computer()
#                 enemy_score = calc_your_score(hand=computers_hand)
#                 calc_winner(user_score, enemy_score)
#         else:
#             running = False


# blackjack()

# # Day 12

# # Number guessing game

# import random

# running = True

# while running:
#     game = input("Do you want to guess the Number??????????. Type 'yes' or 'no': ")
#     if game == "yes":
#         print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
#         random_number = random.randrange(1,101) #to include 100 we have to declare the range of 101
#         choose_difficulty = input("Choose a difficulty. Type 'easy' for 10 attempts or 'hard' for only 5 attempts: ")
#         if choose_difficulty == "easy":
#             attempts = 10
#             while attempts > 0:
#                 guess = int(input("Make a Guess: "))
#                 if guess > random_number:
#                     print("Too high.\nGuess again.")
#                     attempts -= 1
#                     print(f"You have {attempts} attempts remaining to guess the number.")
#                 elif guess < random_number:
#                     print("Too low.\nGuess again.")
#                     attempts -= 1
#                     print(f"You have {attempts} attempts remaining to guess the number.")
#                 else:
#                     print(f"You got it! The answer was {guess}")
#                     attempts = 0
#         else:
#             choose_difficulty == "hard"
#             attempts = 5
#             while attempts > 0:
#                 guess = int(input("Make a Guess: "))
#                 if guess > random_number:
#                     print("Too high.\nGuess again.")
#                     attempts -= 1
#                     print(f"You have {attempts} attempts remaining to guess the number.")
#                 elif guess < random_number:
#                     print("Too low.\nGuess again.")
#                     attempts -= 1
#                     print(f"You have {attempts} attempts remaining to guess the number.")
#                 else:
#                     print(f"You got it! The answer was {guess}")
#                     attempts = 0
#     else:
#         running = False


# # Higher Lower program

# from game_data import data
# import random
# from art import logo4
# from art import vs

# new_celebs = []
# offer = []

# def trigger_new_celeb():
#     new_celebs.append(random.choice(data))

# def trigger_new_offer():
#     offer.append(random.choice(data))

# def game():
#     running = True
#     score = 0
#     trigger_new_celeb()

#     while running:
#         trigger_new_offer()
#         if new_celebs[0] == offer[score]:
#             offer.pop(score)
#             offer.append(random.choice(data))
#         print(logo4)
#         print(f"Compare A: {new_celebs[0]['name']}, {new_celebs[0]['description']}, {new_celebs[0]['country']}")
#         print(vs)
#         print(f"Against B: {offer[score]['name']}, {offer[score]['description']}, {offer[score]['country']}")
#         guess = input("Who has more followers? Type 'A' or 'B': ")
#         if guess == "A":
#             if new_celebs[0]["follower_count"] > offer[score]["follower_count"]:
#                 score += 1
#                 print(f"You're right! Current score {score}")
#             else:
#                 print(f"Sorry, that's not correct. Final score {score}")
#                 running = False
#         elif guess == "B":
#             if offer[score]["follower_count"] > new_celebs[0]["follower_count"]:
#                 new_celebs[0] = offer[score]
#                 score += 1
#                 print(f"You're right! Current score {score}")
#             else:
#                 print(f"Sorry, that's not correct. Final score {score}")
#                 running = False
#         else:
#             print(f"Sorry, that's not 'A' or 'B'. Final score {score}")
#             running = False

# game()

# # Day 15 Coffee Machine Program

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# # starting resources in the machine, also included money
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0,
# }

# COIN_VALUES = {
#     "quarter": 0.25,
#     "dime": 0.10,
#     "nickel": 0.05,
#     "penny": 0.01,
# }
# def payment(number_of_quarters, number_of_dimes, number_of_nickel, number_of_pennies, coffee): #add the number of coins together and reduce the amount of the coffee price
#         amount_quarter = number_of_quarters * COIN_VALUES["quarter"]
#         amount_dimes = number_of_dimes * COIN_VALUES["dime"]
#         amount_nickel = number_of_nickel * COIN_VALUES["nickel"]
#         amount_pennies = number_of_pennies * COIN_VALUES["penny"]
#         payback_money = round((amount_quarter + amount_dimes + amount_nickel + amount_pennies) - coffee["cost"], 2)
#         if payback_money < 0:
#             print("Sorry that's not enough money. Money refunded.")
#             coffee_machine()
#         else:
#             return payback_money

# def suffcient(resources, coffee_ingredients): #resource suffcient check
#     for key in resources:
#         for other_key in coffee_ingredients:
#             if key == other_key:
#                 resources[key] -= coffee_ingredients[other_key]
#                 if resources[key] < 0:
#                     print(f"Sorry there is not enough {key}")
#                     coffee_machine()


# def coffee_machine():
    
#     running = True
    
#     while running:
#         #get the input by the user which coffee he likes to get as variable
#         pick_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         #print function for the actual resources
#         if pick_coffee == "off":
#             running = False
#         elif pick_coffee == "report":
#             for key in resources:
#                 print(f"{key}: {resources[key]}")
#             coffee_machine()
#         else:
#             coffee = MENU[pick_coffee]
#             coffee_ingredients = coffee["ingredients"]
#             #get the input of the amount of coins the user wants to put into the machine
#             print("Please insert coins")
#             number_of_quarters = int(input("How many quarters?: "))
#             number_of_dimes = int(input("How many dimes?: "))
#             number_of_nickel = int(input("How many nickle?: "))
#             number_of_pennies = int(input("How many pennies?: "))
#             payed = payment(number_of_quarters, number_of_dimes, number_of_nickel, number_of_pennies,coffee)
#             suffcient(resources, coffee_ingredients)
#             resources["money"] += coffee["cost"]
#             print(f"Here is {payed}€ in change")
#             print(f"Here is your {pick_coffee}. Enjoy!")

# coffee_machine()

# Day 16

#import turtle
# from turtle import Turtle, Screen

# timmy = Turtle() #fetched turtle class
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen() #defining object (my_screen) of a blueprint, class (Screen)
# print(my_screen.canvheight) #object (myscreen) + attribute/variable (canvheight)
# my_screen.exitonclick() # object (myscreen) + method/function (exitonclick)

# from prettytable import PrettyTable 

# table = PrettyTable() #created new object
# table.add_column("Pokemon Name", ["Pikachu","Schiggi","Glumanda"]) #calling the add_column method
# table.add_column("Type", ["Elektro","Wasser","Feuer"])
# table.align = "l" #changed the alignment to left with changing the aatribute
# print(table)

# good to know: attributes are changeable like variables, methods are not. You can also print the attributes of the object

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

running = True

while running:
    options = new_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        running = False
    elif choice == "report":
        coffee_maker.report() #report method automatically prints the resources
        money_machine.report() #report method automatically prints the amount of money
    else:
        user_choice = new_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(user_choice) and money_machine.make_payment(user_choice.cost):
            coffee_maker.make_coffee(user_choice)