"""
Write a python function to print first N terms of Fibonacci series (TSRN)
"""

# defining a function "print_fib_terms()" which takes a number as an argument
# and print all the terms of fibonacci series
def print_fib_terms(N):
    a, b = 0,1
    print(a,b,end=' ')
    while N != 2:
        add = a + b
        print(add, end=' ')
        a,b = b, add
        N -= 1
        
# taking input from the user
N = int(input("Enter a number : "))

# calling print_fib_terms() to print fibonacci terms
print_fib_terms(N)