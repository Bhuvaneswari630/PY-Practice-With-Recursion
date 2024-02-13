# Write code for algorithm 3 below
# Write a function that returns the nth elements in the Fibonacci Sequence.
def fib(n):
    #  base cases
    if n <= 0:
        return 
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # recursive case
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(8))