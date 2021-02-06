# pforcs-problem-sheet.py
# Author Maria Carroll
# Lecturer: Andrew Beatty

# This readme contains information regarding a series of problems and their solutions:
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

## Description:
