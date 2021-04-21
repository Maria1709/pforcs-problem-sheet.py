# Author Maria carroll
# Week 2
# https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
# Lecture 2 Statements
# Lecturer: Andrew Beatty



#Here we are writng a program to take information from the user to assertain a bmi result from their input 

height = float(input ("Enter height in metres: "))
weight = float(input ("Enter weight in in kg: " ))  

# Below is the formula for calulating bmi

bmi = weight/(height**2)

print("Your BMI is: {0} and you are: ".format(bmi), end='')

# Conditions

if ( bmi < 16):
   print("obese")

elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy weight")

elif ( bmi >= 25 and bmi < 30):
   print("overweight")

elif ( bmi >=30):
   print("obese")

