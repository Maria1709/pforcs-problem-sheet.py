
pforcs|File|problem sheet
-----|----|-----------
**Topic1**|bmi.py|Week2 Problem Sheet - Modify the script to return the bmi: bmi = weight/(height**2)
**Topic2**|email.py|Week2 Problem Sheet - Modify the script to send an email via gmail
**Topic3**|bitcoin.py|Week 3 Problem Sheet - Modify the script to get the up to date 
**Topic4**|Collatz Conjecture|Week4 Problem Sheet -Write a Python script that performs a sequence that repeatedly beginning with a postive integer and taking the result as the input at the next.
**Topic4**|Project Euler 5|Week5 Problem Sheet - Write a Python program using for and range to calculate the smallest possible number that is evenly devisable by all of the numbers from 1-20.
**Topic5**|Openfile.py|Week6 Problem SHeet - Write a Python script that reads the Iris data set and prints the four numerical values on each row in a nice format, Petal width, Petal length,Sepal length and Sepal width.
**Topic6**|Function.py|Week7 Problem Sheet - Write a Pyhton script conataining a function called (factorial) that takes a single input/argument which is a positive integer and returns its factorial.With values 5,7 and 10.


# Author Maria Carroll
# Lecturer: Andrew Beatty

# 1: BMI
# 2: Email
# 3: Bitcoin
# 4: Collatz

# BMI

## Here we are writng a program to take information from the user to assertain a bmi result from their input 

### 
# Below is the formula for calculating bmi

bmi = weight/(height**2)

print("Your BMI is: {0} and you are: ".format(bmi), end='')

### These are the conditions we are using:
### if bmi is over 16 print obese
if ( bmi < 16):
   print("obese")
### if bmi is under equal to 16b or under 18.5 print underweight
elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")
### else if bmi is over  or = to 18.5 but under 25 print healthy weight
elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy weight")
### else if bmi is over or = to 25 but under 30 print overweight
elif ( bmi >= 25 and bmi < 30):
   print("overweight")
### else if bmi is over 30 print obese
elif ( bmi >=30):
   print("obese")
   
   
 # Email
 
 ## Here we are going to send an email via gmail

## import smtplib
import smtplib

## input email address
username = 'mariacarroll3527@gmail.com'
password = 'notsecure'
toEmail = 'G00364700@gmit.ie'
message = ' hi there'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(FROM_EMAIL_ADDRESS,TO_EMAIL_ADDRESS,MESSAGE)


# Bitcoin

## Description : Get the current bitcoin price

#Import the requests library
import requests

## get the URL ticker to get the .json file of the crypto currency
TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

## Function to get the latest crypto currency price for a secific crypto( bitocin. litecoin, ethereum)
def get_latest_crypto_price(crypto):

    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()

    return float(response_json[0]['price_usd']

## Test the function
get_latest_crypto_price('bitcoin')

def main()

    crypto = "bitcoin"
    price = get_latest_crypto_price(crypto)

    print('Bitcoin Price:',price)

main()


# Collatz

## Description: The number we will perform the Collatz operations on.
n = int(input("Enter a positive integer: "))

# Keep looping until we reach 1.
# note: this assumes the Collatz conjecture is true.
while n != 1:
    # Print the current value of n.
    print (n)
    # Check if n is even.
    if n % 2 == 0:
        # If n is even, devide it by two.
        n = n // 2
    else:
        # If n is odd, multiply by three and add 1.
         n = (3 * n) + 1

# Finally, print the 1.
print (n)

# Terminal print out below

PS C:\Users\maria\OneDrive\Desktop\Programming\pforcs-problem-sheet.py> python .\Collatz.py
Enter a positive integer: 10
10
5
16
8
4
2
1
PS C:\Users\maria\OneDrive\Desktop\Programming\pforcs-problem-sheet.py> 
