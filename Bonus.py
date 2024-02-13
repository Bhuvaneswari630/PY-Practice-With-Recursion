#  find greatest common divisor of two numbers
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a%b)
    
a = 56
b = 42
print(greatest_common_divisor(a,b))
