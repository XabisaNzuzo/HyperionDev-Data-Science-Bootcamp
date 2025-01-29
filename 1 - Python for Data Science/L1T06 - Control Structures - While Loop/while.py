def main():
    numbers = []
    
    while True:
        try:
            user_input = float(input("Enter a number (-1 to stop): "))
            
            if user_input == -1:
                break
            
            numbers.append(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average of the entered numbers is: {average}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()