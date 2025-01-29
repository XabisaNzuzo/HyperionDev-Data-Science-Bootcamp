'''write a program that reads the data from the text file
provided (DOB.txt) and prints it out in two different sections in the format
displayed below'''
names = []
birthday = []

file = open("DOB.txt", "r")
data = file.readlines()

for line in data:
    parts = line.split()
    names.append(parts[:2])  # create a variable to store a name
    birthday.append(parts[2:])  # create a variable to store birthday

file.close()

print("Name")
for i, name in enumerate(names):
    print("{}. {}".format(i, " ".join(name)))

print("Birthday")
for i, birthday in enumerate(birthday):
    print("{}. {}".format(i, " ".join(birthday)))