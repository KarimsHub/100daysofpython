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