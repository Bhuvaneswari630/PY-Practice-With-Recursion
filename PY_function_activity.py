# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(*nums):
    num1, num2, num3 = nums
    if num1 > num2:
        if num1 > num3:
            # print(num1, 'is greatest number')
            return num1
    else:
        if num2 > num3:
            # print(num2, 'is greatest number')
            return num2
        else:
            # print(num3, 'is greatest number')
            return num3

print('max number in 1,2,3 is ',max_num(1,2,3))
print('max number in 4,2,3 is ',max_num(4,2,3))
print('max number in 4,8,3 is ',max_num(4,8,3))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(my_list):
    if len(my_list) == 0:
        return 0
    product = 1
    for num in my_list:
        product = product * num
    return product
my_list = [1,2,3,5,6,7]
print('Product of ',my_list, ' is ',mult_list(my_list))
my_list = [4,5,6]
print('Product of ',my_list, ' is ',mult_list(my_list))
my_list = [4]
print('Product of ',my_list, ' is ',mult_list(my_list))
my_list = []
print('Product of ',my_list, ' is ',mult_list(my_list))

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    reverse = ''
    for i in range(len(str)-1, -1, -1):
        reverse = reverse + str[i]
    return reverse
my_str = 'robot'
print('Reverse of ', my_str, ' is ',rev_string(my_str))
my_str = 'Hello'
print('Reverse of ', my_str, ' is ',rev_string(my_str))
my_str = ''
print('Reverse of ', my_str, ' is ',rev_string(my_str))

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num, min, max):
    if num >= min and num <= max:
        return True
    return False

print('2 is in range 1 and 3 -',num_within(2,1,3))
print('1 is in range 1 and 3 -',num_within(1,1,3))
print('5 is in range 1 and 3 -',num_within(5,1,3))
print('3 is in range 1 and 3 -',num_within(3,1,3))
print('0 is in range 1 and 3 -',num_within(0,1,3))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(row):
    if row < 1:
        return print('Invalid number of rows')
    triangle = []
    for i in range(row):
        triangle_element = []
        for j in range(i+1):
            if j == 0 or j == i:
                triangle_element.append(1)
            else:
                triangle_element.append(triangle[i-1][j-1]+triangle[i-1][j])
        triangle.append(triangle_element)
    triangle
    for row in triangle:
        print(row)
row = 7
print('Pascal Triangle of ', row, ' rows')        
pascal(row)
row = 4
print('Pascal Triangle of ', row, ' rows')        
pascal(row)
row = -1
print('Pascal Triangle of ', row, ' rows')        
pascal(row)



    
