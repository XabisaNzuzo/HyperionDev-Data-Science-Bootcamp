#Prompt the user for an input

str_manip = input("Please enter a sentence: ")
string_length = len(str_manip)
print("The length of the sting is: ", string_length)
last_letter = str_manip[-1]

# Replaces the occurrence of the last letter with '@'

modified_str = str_manip.replace(last_letter, '@')
print("The modified sentence is:", modified_str)

# Print the last three characters in str_manip backwards

last_three_reversed = str_manip[-3:][::-1]
print("The last 3 characters in reverse are:", last_three_reversed)

# This creates a five-letter word made up of the first three characters and the last two characters

five_letter_word = str_manip[:3] + str_manip[-2:]
print("The five-letter word is:", five_letter_word)
