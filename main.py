#Day 1: Creating Band Name Generator
print("Welcome to the Band Name Generator.")
cityname = input("What's name of the city you grew up in? \n")
petsname = input("What's your pet's name? \n")
print("Your band name could be " + cityname + " " + petsname)

#Day 2:
# BMI Calculator:
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
