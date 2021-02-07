import smtplib
import sys
sys.path.append(C:\Users\maria\OneDrive\Desktop\gmit\email details)
import details # The password and the email are stored outside of git folder 
server = smtplib.SMTP_SSL('smtp.gmail.com',587)
FROM_EMAIL_ADDRESS = input('Who is sending the email?')
TO_EMAIL_ADDRESS = input('Who are you sending the email to?')
SUBJECT= input("Enter the subject of the email")
TEXT = input('Write your message')
MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
server.login(details.username,details.password)
server.sendmail(FROM_EMAIL_ADDRESS,TO_EMAIL_ADDRESS,MESSAGE, SUBJECT)
