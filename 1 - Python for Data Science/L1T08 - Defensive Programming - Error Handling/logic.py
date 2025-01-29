# This function checks if the number is an even number or odd number

def check_even_odd(number):
    if number % 2 == 1:  # Logic error: check if the number modulo 2 equals 1 to deteremine if the number is even, which is incorrect. 
        return "Even"
    else:
        return "Odd"

# Test the function with different values

numbers_to_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers_to_test:
    result = check_even_odd(number)
    print(f"The number {number} is {result}.")