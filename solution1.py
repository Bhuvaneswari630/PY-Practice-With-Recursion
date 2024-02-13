# Write code for algorithm 1 below
# Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def alg1(n):
    # base case
    if n < 0:
        return 0
    # recursive case
    else:
        print(n)
        alg1(n-1)

alg1(8)