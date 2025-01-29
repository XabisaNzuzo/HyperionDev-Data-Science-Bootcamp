# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error: added parentheses () after print 
print("\n")  # Syntax error: there were no paranthesis

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = 24   # Compilation error: incorrect space indetaion for both 'age_Str' and 'age' # Syntax error: Corrected the string format comparison operator == should be the assignment operator =.
age = int(age_Str)    

print("I'm" + str(age) + "years old.")   #  Syntax error: concatenation of strings and integers needs to be handled properly.

# Variables declaring additional years and printing the total years of age
years_from_now = 3  # Syntax error: Inorrect Indentation
total_years = age + int(years_from_now)   # Syntax rrected the casting and addition
               

print ("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = int(total_years) * 12  # Syntax error: Changed the variable name from total to total_year
print("In 3 years and 6 months, I'll be " + str(total_months + 6) +" months old")  # Sytnax error : There were no paranthesis) and runtime error

#HINT, 330 months is the correct answer

