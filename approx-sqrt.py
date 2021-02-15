#Adapted from:https://tour.golang.org/flowcontrol/8

def sqrt(x):
    # Initial guess,
    z = 1.0
    
    # Keep getting a better estimate for the square root
    # of x until you are within two decimal places.
    # While the difference between those two numbers is greater than or equal to 
    # 0.01. want to be 0.01 close to 0
    while abs(z*z - x) >= 0.01:
        # Get a better apporximation for the square root. by multiplying z by itself should get a very close or even the exact value of x.
        z -= (z*z - x) / (2*z)

    return z
# Calculate the square root of 8

z = (sqrt(8.0))
# Print z
print (z)
# Print the square root of the square of z.
print(z*z)
# Only an approximation
# We are runnning an algorithm that performs a loop,
#  a while loop, our algorithm finds an approximation of the answer. Newtons method is a root finding algorithm, 
# that always comes to an end.