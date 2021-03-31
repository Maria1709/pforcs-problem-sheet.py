
pforcs|Problem title|Problem sheet
-----|----|-----------
**Topic1**|bmi.py|Week1 Problem Sheet - Modify the script to return the bmi: bmi = weight/(height**2)
**Topic2**|email.py|Week2 Problem Sheet - Modify the script to send an email via gmail
**Topic3**|bitcoin.py|Week 3 Problem Sheet - Modify the script to get the up to date 
**Topic4**|Collatz Conjecture|Week4 Problem Sheet -Write a Python script that performs a sequence that repeatedly beginning with a postive integer and taking the result as the input at the next.
**Topic5**|approx-sqrt.py|Week 5 Problem Sheet - Write a Python Program that takes a positive floating-point number as input and outputs an approximation of its square root.
**Topic6**|moby.py|Week6 Problem Sheet - Write a program that reads in a text file and outputs the number of e's it contains.
**Topic7**|ExtractURL.py|Week7 Problem Sheet -  Write a program called extract-url.py, that will extract the URLs from an access.log file.
**Topic8**|Plottask.py|Week8 Problem Sheet - Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. 
**Topic9**|SessionId|Week9 Problem Sheet - I want to find which sessionId downloaded the most data
**Topic10**|Funcitons| Week10 Problem Sheet - Write a (bullet proof) function called averageTo(aList, toIndex)


# Author Maria Carroll
# Lecturer: Andrew Beatty

# 1: BMI
## Write a program that calculates somebody's Body Mass Index (BMI).The inputs are the person's height in centimetres and weight in kilograms.The output  is their weight divided by their height in metres squared.$ python bmi.pyEnter weight: 65Enter height: 180BMI is 20.06.
# 1: Email: Set up a Gmail account, and write a python program to send an email from it.Modify the program to read in the to-Email address, subject,  and message
# 2: Bitcoin
## Write a program (bitcoin.py) that prints out todays bitcoin price in dollars.
# 3: Collatz
## Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.Have the program end if the current value is one.$ python collatz.pyPlease enter a positive integer: 1010 5 16 8 4 2 1
# 4: Functions
## Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.You should create a function called <tt>sqrt</tt> that does this.I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)I suggest that you look at the newton method at estimating square roots$ python squareroot.pyPlease enter a positive number: 14. The square root of 14.5 is approx. 3.8.
# 5: Moby
## Write a program that reads in a text file and outputs the number of e's it contains.The program should take the filename from an argument on the command line.$ python es.py moby-dick.txt116960
# 7: Extract URL
## Write a program called extract-url.py, that will extract the URLs from an access.log file.ie The part of the URL that is stored in the access.log file, complete with the query parameters (I am aware that the host name is not stored in this file, the referring host is)The program should store the URLs as strings in a list'/cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958','/category.screen?categoryId=SHOOTER&JSESSIONID=SD7SL9FF5ADFF5066']
# 8: Plottask
## Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.Some marks will be given for making the plot look nice.
# 9: Sessionid
## I want to find which sessionId downloaded the most dataRead the access.log into a dataframe (see lab)Set the date time to be the index (you will need to manipulate this data, see lab)Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)Use groupBy to get the sum of all the data downloaded by each sessionId.Create a plot of this (type of your choice)
# 10: Errors
## Write a (bullet proof) function called averageTo(aList, toIndex)The function should take in a list and an index. The function will return the average of the numbers upto and including the toIndex in the aList.When I say "bullet proof", I would like the function to always return an integer, even if a error oc



# References
   # 
	# https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
	# https://automatetheboringstuff.com/chapter3/
	# https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
	# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
	# https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
	#


