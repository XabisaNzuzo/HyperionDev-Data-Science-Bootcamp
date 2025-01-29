# request id number of students and read total students registering
number_students = int(input('Number of students registering: '))

# output file to store all IDs

file_name = open("reg_form.txt", "w")
for i in range(number_students):

    # Prompt and read student ID
    ID = input("Enter your ID number:")

    # write the ID in file
    file_name.write(ID+'\n')
    file_name.write("-" * 20 + "\n") # Add dotted line after ID number

# Close the file
file_name.close()

