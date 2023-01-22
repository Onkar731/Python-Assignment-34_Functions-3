"""
Write a python function to print all factors of a given number (TSRN)
"""

# defining a function "print_all_factors()" which takes a number as an argument
# and prints all the factors of the number
def print_all_factors(num):
    print("Factors : 1", end=' ')
    for e in range(2, num+1):
        if num%e == 0:
            print(e, end=' ')
            

# taking input from the user
num = int(input("Enter a number :"))

# calling print_all_factors() to print all factors of the given number
print_all_factors(num)