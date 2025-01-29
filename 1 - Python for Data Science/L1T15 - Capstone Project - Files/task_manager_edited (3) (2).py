from datetime import date, datetime
import os

# Read users from user.txt and populate the dictionary
def read_users():
    login_details = {}
    if not os.path.exists("user.txt"):
        open("user.txt", "w").close()  # Create file if it does not exist

    with open("user.txt", "r") as file:
        for line in file:
            try:
                name, password = line.strip().split(", ")
                login_details[name] = password
            except ValueError:
                print(f"Skipping malformed line in user.txt: {line.strip()}")
    return login_details

# Write new user to user.txt
def write_user(username, password):
    with open("user.txt", "a") as file:
        file.write(f"{username}, {password}\n")

# Read tasks from tasks.txt and return as a list of lists
def read_tasks():
    tasks = []
    if not os.path.exists("tasks.txt"):
        open("tasks.txt", "w").close()  # Create file if it does not exist

    with open("tasks.txt", "r") as file:
        for line in file:
            try:
                tasks.append(line.strip().split(", "))
            except ValueError:
                print(f"Skipping malformed line in tasks.txt: {line.strip()}")
    return tasks

# Write new task to tasks.txt
def write_task(task_info):
    with open("tasks.txt", "a") as file:
        file.write(", ".join(task_info) + "\n")

# Display tasks in a readable format
def display_tasks(tasks):
    for task in tasks:
        person, title, description, date_assigned, due_date, completed = task
        print(f"Assigned to: {person}\nTitle: {title}\nDescription: {description}\nDate Assigned: {date_assigned}\nDue Date: {due_date}\nCompleted: {completed}\n")

# Include the 's' option for statistics
def display_statistics():
    tasks = read_tasks()
    total_tasks = len(tasks)
    compelted_tasks = sum(1 for task in tasks if tasks[-1] == "Yes")
    
    print(f"Total number of tasks: {total_tasks}\n")
    print(f"Completed tasks: {compelted_tasks}\n")
    print(f"Remaining tasks: {total_tasks - compelted_tasks}")


# Main program loop
def main():
    login_details = read_users()
    username = None
    
    # User authentication loop
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in login_details and login_details[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
    
    while True:
        print("\nPlease select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        if username == 'admin':  # Show option only to admin
         print("s - view statistics")
        print("e - exit")

        option = input("Enter your choice: ").lower()



        if option == 'r' and username == 'admin':
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            write_user(new_username, new_password)
            print("New user registered successfully!")
        elif option == 'a':
            task_user = input("Enter the username of the person the task is assigned to: ")
            task_title = input("Enter the title of the task: ")
            task_description = input("Enter the description of the task: ")
            date_assigned = date.today().strftime("%Y-%m-%d")
            task_due_date = input("Enter the due date of the task (e.g., 2024-10-10): ")
            try:
                due_date_obj = datetime.strptime(task_due_date, "%Y-%m-%d")
                if due_date_obj < datetime.now():
                    print("Due date cannot be in the past. Please enter a valid due date.")
                    continue
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            task_completed = "No"
            task_info = [task_user, task_title, task_description, date_assigned, task_due_date, task_completed]
            write_task(task_info)
            print("Task added successfully!")
        elif option == 'va':
            tasks = read_tasks()
            if tasks:
                display_tasks(tasks)
            else:
                print("No tasks found.")
        elif option == 'vm':
            tasks = read_tasks()
            user_tasks = [task for task in tasks if task[0] == username]
            if user_tasks:
                display_tasks(user_tasks)
            else:
                print("You have no tasks assigned.")
        elif option == 'e':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
