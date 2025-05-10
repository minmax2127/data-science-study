'''  PASSWORD CHECKER

Enter password: <user input>

Strength: <percentage>

/ Atleast 12 characters long  100%
Combination of:   100%
    / uppercase    25%
    / lowercase    25%
    / numbers      25%
    / symbols      25%
    
'''

# displays the qualifications and whether it has been achieved
def checkbox_requirement(requirement, is_check, char_count, is_len = False):
    if is_check:
        print("\t / ", end="")
    else:
        print("\t X ", end="")

    if is_len:
        print(requirement + " (" + str(char_count) + ")")
    else: 
        if char_count > 0:
            print(requirement + " (" + str(char_count) + ")")
        else:
            print(requirement)

# calculates password strength by getting the average of length percentage and chartype percentage
def calculate_strength_percentage(length, char_types):

    # char percentage calculated by adding 25% for each char_type(uppercase, lowercase, number, symbol) and summing up to 100%
    type_count = 0
    for x in char_types:
        if x:
            type_count += 1
    char_percentage = type_count * 25

    # length percentage calculated by having 100% for 12 characters and above. the percentage decreases the less character there is below 12
    length_percentage = 100
    min_count = 12
    if length < min_count: 
        length_percentage = 100 - ((min_count - length) * 100/min_count)

    # average of the two percentages
    percentage = (length_percentage + char_percentage) / 2


    return percentage


''' MAIN FUNCTION'''

# set up a base to assess whether a password is secure enough
# if password strength is below 75%, the program will prompt the user to input a new password again 
secure_percentage_base = 75.00  

while True:
    print("\n---------------------------------")
    password = input("\nEnter password: ")
    strength_percentage = 0.00
    
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    symbol_count = 0
    space_count = 0


    # iterates through every character in a string
    for c in password:
        ascii = ord(c)  # takes ascii code of a character
        if ascii == 32:
            space_count += 1
        elif ascii >= 123:
            symbol_count += 1
        elif ascii >= 97:
            lowercase_count += 1
        elif ascii >= 91:
            symbol_count += 1
        elif ascii >= 65:
            uppercase_count += 1
        elif ascii >= 58:
            symbol_count += 1
        elif ascii >= 48:
            number_count += 1
        elif ascii >= 33:
            symbol_count += 1

    # RESULTS

    # automatically declares an input wrong if it contains a space
    if space_count > 0:
        print("Invalid password! You cannot use a space.")
        continue

    # calculates strength percentage
    strength_percentage = calculate_strength_percentage(len(password), [uppercase_count > 0, lowercase_count > 0, number_count > 0, symbol_count > 0])
    print("\n    Strength Percentage: " + str(strength_percentage) + "%")


    # length check
    print()
    checkbox_requirement("has atleast 12 characters", len(password) >= 12, len(password), True)
    print()

    # character check
    checkbox_requirement("contains uppercase letter/s", uppercase_count > 0, uppercase_count)
    checkbox_requirement("contains lowercase letter/s", lowercase_count > 0, lowercase_count)
    checkbox_requirement("contains number/s", number_count > 0, number_count)
    checkbox_requirement("contains symbol/s", symbol_count > 0, symbol_count)
    print()

    # space check
    checkbox_requirement("has no space", space_count == 0, space_count)


    
    # checks if password is good enough to pass the qualification check
    if(strength_percentage >= 75.00):
        print("\n Your password has passed the qualification check. \n")
        break
    else:
        print("\n Please try again, your password is not secure enough. \n")
