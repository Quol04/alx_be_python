# Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_msg = "This is a high-priority task."
    case "medium":
        priority_msg = "This is a medium-priority task."
    case "low":
        priority_msg = "This is a low-priority task."
    case _:
        priority_msg = "Priority level not recognized."


if time_bound == "yes":
    print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    # time_msg = "Make sure to complete it as soon as possible!"
else:
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    # time_msg = "You can take your time with this task."


# print(priority_msg)
# print(time_msg)