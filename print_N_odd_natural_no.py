"""
Write a python function to print first N odd natural numbers (TSRN)
"""

# defining a function "print_odd_natural()" which takes a number as an argument
# and printing numbers
def print_odd_natural(N):
    for e in range(1,N+1):
        print(e*2-1, end=' ')
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_odd_natural() to print odd natural numbers
print_odd_natural(N)