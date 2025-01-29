 
# Prompt the user to enter the time taken for swimming

swimming_time = int(input("Enter the time taken for swimming (in minutes): "))

# Prompt the user to enter the time taken for cycling

cycling_time = int(input("Enter the time taken for cycling (in minutes): "))

# Prompt the user to enter the time taken for running

running_time = int(input("Enter the time taken for running (in minutes): "))

# Calculate the total time taken to complete the triathlon

total_time = swimming_time + cycling_time + running_time

# Print out the total time taken TO complete the triathlon

print(f"The total time taken to complete the triathlon is: {total_time} minutes")

# Step 6: Determine the award based on the total time taken

if total_time <= 100:
    print("Provincial Colours")
elif total_time <= 105:
    print("Provincial Half Colours")
elif total_time <= 110:
    print("Provincial Scroll")
else:
    print("No award")