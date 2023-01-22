"""
Write a python function to print all prime numbers between two given numbers (TSRN)
"""

# defining a function to check whether the number is prime or not
# which takes a number as an argument and returns True or False
def is_prime(num):
    i = 2
    while i<num:
        if num%i == 0:
            return False
        i += 1
    if i == num:
        return True


# defining a function "print_all_prime()" which takes two number as an argument
# and print all prime numbers between two given numbers
def print_all_prime(start, end):
    while start <= end:
        if is_prime(start):
            print(start, end=' ')
        start += 1
        

# taking input from the user
start, end = int(input("Enter start and end number to print all prime numbers : ")), int(input())

# calling print_all_prime() to print all prime numbers
print_all_prime(start, end)