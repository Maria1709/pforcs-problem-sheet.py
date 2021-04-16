# Author: Maria Carroll
# Week 4
# https://docs.python.org/3/tutorial/controlflow.html
# Lecture: Controlling the flow
# Lecturer: Andrew Beatty



# The number we will perform the Collatz operations on.
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
