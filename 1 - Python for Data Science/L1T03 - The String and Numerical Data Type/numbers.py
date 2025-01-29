#Prompt user for 3 different numbers

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

# This calculates and print out the sum of all the numbers

total_sum = num1 + num2 + num3
print("The sum of all the numbers is:", total_sum)

# This calculates and print the first number minus the second number

difference = num1 - num2
print("The first number minus the second number is:", difference)

# This calculates and print the third number multiplied by the first number

product = num3 * num1
print("The third number multiplied by the first number is:", product)

#This calculates and print the sum of all three numbers divided by the third number

division = total_sum / num3
print("The sum of all three numbers divided by the third number is:", division)
