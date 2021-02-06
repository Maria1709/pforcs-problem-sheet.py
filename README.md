# pforcs-problem-sheet.py
# Author Maria Carroll
# Lecturer: Andrew Beatty

# This readme contains inforamtion regarding a series of problems and their solutions:
# 1: BMI
# 2: Email
# 3: Bitcoin
# 4: Collatz

## Here we are writng a program to take information from the user to assertain a bmi result from their input 

### 
# Below is the formula for calulating bmi

bmi = weight/(height**2)

print("Your BMI is: {0} and you are: ".format(bmi), end='')

### These are the conditions we are using:

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


