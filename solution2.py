# Write code for algorithm 2 below
# Write a function that prints the natural numbers from 1 to n.
def natural_numbers(n, i=1):
    #  base case
    if i > n:
        return
    #  recursive case
    else:
        print(i)
        natural_numbers(n, i+1)
natural_numbers(10)