# Prompt the user their full name
full_name = input("Please enter your full name: ")

# This is for validation checks
if len(full_name.strip()) == 0:
    print("You have not entered anything. Please enter your full name.")
elif len(full_name.strip()) < 4:
    print("You have entered less than 4 characters. Please ensure that you have entered your name and surname.")
elif len(full_name.strip()) > 25:
    print("You have entered more than 25 characters. Please ensure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")