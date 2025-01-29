# Importing required modules
import datetime

# Function to read users from user.txt
def read_users():
    users = {}
    with open("user.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users

# Function to write user to user.txt
def write_user(username, password):
    with open("user.txt", "w") as file:
        file.write(f"{username}, {password}\n")

# Function to read tasks from tasks.txt
def read_tasks():
    tasks = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_info = line.strip().split(", ")
            tasks.append(task_info)
    return tasks

# Function to write task to tasks.txt
def write_task(task_info):
    with open("tasks.txt", "a") as file:
        file.write(", ".join(task_info) + "\n")

# Function to display tasks in an easy-to-read format
def display_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        username, title, description, date_assigned, due_date, completed = task
        print(f"Task {i}:\nAssigned to: {username}\nTitle: {title}\nDescription: {description}")
        print(f"Date assigned: {date_assigned}\nDue date: {due_date}\nCompleted: {completed}\n")

# Function to calculate statistics and display them in a user-friendly manner
def display_statistics(tasks, users):
    total_tasks = len(tasks)
    total_users = len(users)
    completed_tasks = sum(1 for task in tasks if task[-1] == "Yes")

    print(f"Total tasks: {total_tasks}")
    print(f"Total users: {total_users}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Uncompleted tasks: {total_tasks - completed_tasks}")

# Main function to handle the task manager program
def main():
    # Read data from files
    users = read_users()
    tasks = read_tasks()

    # Login
    logged_in = False
    while not logged_in:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print(f"Welcome, {username}!")
            logged_in = True
        else:
            print("Invalid username or password. Please try again.")

    # Display the menu options
    print("\nMenu:")
    print("r - Register User" if username == "admin" else "")
    print("a - Add Task")
    print("va - View All Tasks")
    print("vm - View My Tasks")
    print("ds - Display Statistics" if username == "admin" else "")
    print("e - Exit")

    # Process user's choice
    while True:
        choice = input("\nEnter your choice: ")

        if choice == "r" and username == "admin":
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm the new password: ")

            if new_password == confirm_password:
                write_user(new_username, new_password)
                print("User registered successfully!")
            else:
                print("Passwords do not match. User not registered.")

        elif choice == "a":
            assigned_to = input("Enter the username of the person the task is assigned to: ")
            title = input("Enter the title of the task: ")
            description = input("Enter a description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            new_task = [assigned_to, title, description, current_date, due_date, "No"]
            write_task(new_task)
            print("Task added successfully!")

        elif choice == "va":
            display_tasks(tasks)

        elif choice == "vm":
            user_tasks = [task for task in tasks if task[0] == username]
            display_tasks(user_tasks)

        elif choice == "ds" and username == "admin":
            display_statistics(tasks, users)

        elif choice == "e":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
