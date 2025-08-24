import csv
from datetime import datetime

TASKS_FILE = "tasks.csv"

# Create tasks.csv file if not present
def init_file():
    try:
        open(TASKS_FILE, "x").close()
    except FileExistsError:
        pass

# Add a new study task
def add_task():
    subject = input("📘 Enter subject name: ")
    task = input("✏️ Enter task description: ")
    deadline = input("📅 Enter deadline (YYYY-MM-DD): ")

    try:
        datetime.strptime(deadline, "%Y-%m-%d")  # validate date
    except ValueError:
        print("⚠️ Invalid date format! Use YYYY-MM-DD.\n")
        return

    with open(TASKS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([subject, task, deadline, "Pending"])
    print("✅ Task added successfully!\n")

# View all tasks
def view_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            reader = csv.reader(file)
            tasks = list(reader)

            if not tasks:
                print("📂 No tasks found! Add something first.\n")
                return

            print("\n===== 📚 Your Study Tasks =====")
            for i, row in enumerate(tasks, 1):
                subject, task, deadline, status = row
                print(f"{i}. {task} ({subject}) - Due: {deadline} [{status}]")
            print()
    except FileNotFoundError:
        print("📂 No tasks file found!\n")

# Mark a task as completed
def mark_done():
    view_tasks()
    try:
        task_no = int(input("✅ Enter task number to mark as done: "))
    except ValueError:
        print("⚠️ Please enter a valid number!\n")
        return

    with open(TASKS_FILE, "r") as file:
        tasks = list(csv.reader(file))

    if 0 < task_no <= len(tasks):
        tasks[task_no - 1][3] = "Done 🎉"
        with open(TASKS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("🎯 Great job! Task marked as completed.\n")
    else:
        print("⚠️ Invalid task number!\n")

# Main menu loop
def main():
    init_file()
    print("✨ Welcome to Student Study Planner ✨")
    while True:
        print("\n===== Main Menu =====")
        print("1️⃣  Add Task")
        print("2️⃣  View Tasks")
        print("3️⃣  Mark Task as Done")
        print("4️⃣  Exit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("👋 Goodbye! Stay consistent with your studies!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
