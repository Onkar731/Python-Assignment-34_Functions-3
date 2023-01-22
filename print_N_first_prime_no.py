"""
Write a python function to print first N prime numbers (TSRN)
"""

# defining a function "print_prime()" which takes a number as an argument
# and printing first N prime numbers
def print_prime(N):
    num = 2
    while N != 0:
        i = 2
        while i*i <= num:
            if num%i == 0:
                break
            i += 1
        else:
            print(num, end=' ')
            N -= 1
        num += 1
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_prime() to print prime numbers
print_prime(N)