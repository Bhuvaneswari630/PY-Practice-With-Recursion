# Write code for algorithm 4 below
# Write a function that calculates the value of 'a' to the power of 'b'.
def power(a, b):
    # base case
    if b == 0:
        return 1
    #  recursive case
    else:
        return a * power(a, b-1)
    
result = power(2,3)
print(result)
