# send an email via gmail
# author maria carrolll
# Lecturer: Andrew Beatty

import smtplib


username = 'mariacarroll3527@gmail.com'
password = 'notsecure'
toEmail = 'G00364700@gmit.ie'
message = ' hi there'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(FROM_EMAIL_ADDRESS,TO_EMAIL_ADDRESS,MESSAGE)

