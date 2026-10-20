"""
Bin2Dec
Tier: 1-Beginner

Binary is the number system all digital computers are based on. Therefore it's important for developers to
understand binary, or base 2, mathematics. The purpose of Bin2Dec is to provide practice and understanding of
how binary calculations.

Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays
its decimal equivalent.

This challenge requires that the developer implementing it follow these constraints:

Arrays may not be used to contain the binary digits entered by the user
Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using a single
mathematical function, for example the natural logarithm. It's up to you to figure out which function to use.

User Stories
    User can enter up to 8 binary digits in one input field
    User must be notified if anything other than a 0 or 1 was entered
    User views the results in a single output field containing the decimal (base 10) equivalent of
    the binary number that was entered
    
Bonus features
    User can enter a variable number of binary digits
"""

# if we want variable number of binary digits, we can remove the string_length() function 
# and just check for invalid characters in wrong_input() function.

"""
def string_length():
    if len (binary_input) > 8:
        print("Error: You can only enter up to 8 binary digits.")
        return False
    return True
"""   
def wrong_input():
    for index, sign in enumerate(binary_input):
        if sign != "0" and sign != "1":
            print(f"Error: Invalid character '{sign}' at position {index + 1}. Please enter only 0's and 1's.")
            return False 
    return True

def calculate_decimal():
    decimal_value = 0
    length = len(binary_input)
    for index, sign in enumerate(binary_input):
        if sign == "1":
            decimal_value += 2**(length - index - 1)
    return decimal_value

print("Welcome to the Binary to Decimal Calculator!")
print("You can enter up to 8 binary digits (0's and 1's) to convert them to decimal.")
print("Please enter your binary number:")
binary_input = input()

# if we want if we want variable number of binary digits, we need also to remove
# the string_length() function from the if statement below.
if """string_length() == True""" and wrong_input() == True:
    decimal_value = calculate_decimal()
    print(f"The decimal equivalent of binary '{binary_input}' is: {decimal_value}")
