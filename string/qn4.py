# Convert a given string to all uppercase and then replace all occurrences of the letter 'A' 
# with the character '@'.


user = input("Enter a string: ")
upper_case_string = user.upper()
print(upper_case_string)
modified_string = upper_case_string.replace('A', '@')
print("Modified string:", modified_string)
