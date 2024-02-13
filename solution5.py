# Write code for algorithm 5 below
# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.
def is_palindrome(str):
    #   base case
    if len(str) <= 1:
        return True
    #  recursive case
    else:
        # return (str[0] == str[-1]) and is_palindrome(str[1:-1])
        return (str[0] == str[len(str)-1]) and is_palindrome(str[1:len(str)-1])
print("is 'Gandalf' a palindrome?")
print(is_palindrome('Gandalf'))
print("is 'rotator' a palindrome?")
print(is_palindrome('rotator'))

def itr_palindrome(str):
    if len(str) <= 1:
        return True
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-1 - i]:
            return False
    return True
print("is 'Gandalf' a palindrome?")
print(itr_palindrome('Gandalf'))
print("is 'rotator' a palindrome?")
print(itr_palindrome('rotator'))