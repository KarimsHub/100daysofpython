# Day 1: Creating Band Name Generator
print("Welcome to the Band Name Generator.")
cityname = input("What's name of the city you grew up in? \n")
petsname = input("What's your pet's name? \n")
print("Your band name could be " + cityname + " " + petsname)

# Day 2:
BMI Calculator:
height = input("What is your height in m? ")
weight = input("What is your weight in kg? ")
bmi =  float(weight) / (float(height)**2)
bmi_rounded = round(bmi)
print(bmi_rounded)

# print(type(6 // 2))
# // = always results an integer
# score = score + 1 == score +=1

# f -strings
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Your life in weeks program
age = input("What is your current age? ")
years_remaining = 90 - int(age)
months = int(years_remaining) * 12
weeks = int(years_remaining) * 52
days = int(years_remaining) * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Tip calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))

percentage_bill = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split_in_people = int(input("How many people to split the bill? "))

first_result = ((total_bill / split_in_people) / 100) * percentage_bill
second_result = ((total_bill / split_in_people) + first_result)
rounded_second_result = round(second_result, 2)

print(f"Each person should pay: €{rounded_second_result}")

# Day 3:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What are your age? "))

    if age < 12:
        bill = 5
        print("child tickets are 5€")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7€")
    else:
        bill = 12
        print("Adult tickets are 12€")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add 3€
        bill += 3
    
    print(f"Your final bill is {bill}")


else:
    print("you can't ride the rollercoaster!")

# BMI Calculator 2.0:

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
bmi_rounded = round(bmi)

if bmi_rounded < 18.5:
    print(f"Your BMI is {bmi_rounded}, you are underweight")
elif bmi_rounded < 25:
    print(f"Your BMI is {bmi_rounded}, you are normal weight")
elif bmi_rounded < 30:
    print(f"Your BMI is {bmi_rounded}, you are slightly overweight")
elif bmi_rounded < 35:
    print(f"Your BMI is {bmi_rounded}, you are obese")
else:
    print(f"Your BMI is {bmi_rounded}, you are clinically obese")

# Leap Year Program
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("This year is not a Leap year")
    else:
        print("This year is a Leap year")    
else:
    print("This year is not a leap year")

# Pizza Order Program
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want some extra cheese? Y or N? ")
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: {bill}")
        else:
           print(f"Your final bill is: {bill}") 
    else:
        print(f"Your final bill is: {bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: {bill}")
        else:
           print(f"Your final bill is: {bill}") 
    else:
        print(f"Your final bill is: {bill}")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: {bill}")
        else:
           print(f"Your final bill is: {bill}") 
    else:
        print(f"Your final bill is: {bill}")
else:
    print("Please try again")

# Love Calculator Program
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
love_score = 0

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()
number_of_t = name1_lower_case.count("t") + name2_lower_case.count("t")
number_of_r = name1_lower_case.count("r") + name2_lower_case.count("r")
number_of_u = name1_lower_case.count("u") + name2_lower_case.count("u")
number_of_e = name1_lower_case.count("e") + name2_lower_case.count("e")
true_score = number_of_t + number_of_r + number_of_u + number_of_e

number_of_l = name1_lower_case.count("l") + name2_lower_case.count("l")
number_of_o = name1_lower_case.count("o") + name2_lower_case.count("o")
number_of_v = name1_lower_case.count("v") + name2_lower_case.count("v")
love_score = number_of_l + number_of_o + number_of_v + number_of_e
new_score = str(true_score) + str(love_score)

if int(new_score) < 10 or int(new_score) > 90:
    print(f"Your score is {new_score}, you go together like coke and mentos")
elif int(new_score) >= 40 and int(new_score) <= 50:
    print(f"Your score is {new_score}, you are alright together")
else:
    print(f"Your score is {new_score}")

# Alice in Wonderland Adventure
print('''                   .'\   /`.
                 .'.-.`-'.-.`.
            ..._:   .-. .-.   :_...
          .'    '-.(o ) (o ).-'    `.
         :  _    _ _`~(_)~`_ _    _  :
        :  /:   ' .-=_   _=-. `   ;\  :
        :   :|-.._  '     `  _..-|:   :
         :   `:| |`:-:-.-:-:'| |:'   :
          `.   `.| | | | | | |.'   .'
            `.   `-:_| | |_:-'   .'
         jgs  `-._   ````    _.-'
                  ``-------''
                  ''')
print("Welcome to the Alice in Wonderland Adventure")
print("Your mission is to escape the Wonderland and resque the helpless Bunny from the Emperor! \nAfter a few minutes of walking you meet a soldier who ask's about your ID")

first_answer = input("Do you want to discuss that you don't have an ID or do you want try to escape with running? Please type \"discuss\" or \"escape\"!: ").lower()
if first_answer == "discuss":
    print("The soldier does not accept the answer and take`s you to the emperor's castle")
    second_answer = input("In the castle you've been locked in a cell with the bunny right next to you. \nYou two are talking for quite a while and the bunny suggests you to overwhelm the guard protecting the cell. \nDo you want to overwhelm or wait for sunrise? Please type \"overwhelm\"or \"wait\"!: ").lower()
    if second_answer == "overwhelm":
        print("You've successfully overwhelmed the guard and escaped the cell with the bunny")
    elif second_answer == "wait":
        print("Game over: Waiting didn't helped you by finding a solution. The bunny died!")
    else:
        print("Game over: You didn't choose one of the given answers!")
elif first_answer == "escape":
    print("Game over: You couldn't escape the soldier and died. Please try again")
else:
    print("Game over: You didn't choose one of the given answers!")

# Day 4

# Heads or Tails program
import random

random_number = random.randint(0, 1)
if random_number == 0:
    print("Tails")
else:
    print("Heads")

# Banker Roulette program
import random

names_string = input("Give me everybody's names, seperated by a comma: ")
names = names_string.split(", ")
#number_of_names = (len(names) -1)
random_number = random.randint(0, (len(names) -1))
print(f"{names[random_number]} is going to buy the meal today!")

# nested list
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]

# Treasure Map Program
row1 = ["😉","😉","😉"]
row2 = ["😉","😉","😉"]
row3 = ["😉","😉","😉"]

map = [row1, row2, row3]
position = input("Where do you want to put the treasure? ")
column_number = (position[0])
row_number = (position[1])

map[int(row_number) -1][int(column_number) -1] = "x"
print(f"{row1}\n{row2}\n{row3}")

# Rock paper scissors game Program

import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
# rock wins against scissors
# scissors win against paper
# paper wins against rock
if your_choice == 0:
    print(rock)
    if computer_choice == 2:
        print(f"Computer chose:\n {scissors}\nYou win!")
    elif computer_choice == 0:
        print(f"Computer chose:\n {rock}\nDraw!")
    else:
        print(f"Computer chose:\n {paper}\nYou lose!")
elif your_choice == 1:
    print(paper)
    if computer_choice == 0:
        print(f"Computer chose:\n {rock}\nYou win!")
    elif computer_choice == 1:
        print(f"Computer chose:\n {paper}\nDraw!")
    else:
        print(f"Computer chose:\n {scissors}\nYou lose!")
elif your_choice == 2:
    print(scissors)
    if computer_choice == 1:
        print(f"Computer chose:\n {paper}\nYou win!")
    elif computer_choice == 2:
        print(f"Computer chose:\n {scissors}\nDraw!")
    else:
        print(f"Computer chose:\n {rock}\nYou lose!")
else:
    print("Please input the right number")