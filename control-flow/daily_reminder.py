# daily_reminder.py

# Step 1: Prompt the user for task details
task = input("Enter your task: ")  # Task description
priority = input("Priority (high/medium/low): ").lower()  # Priority level
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Time sensitivity

# Step 2: Initialize the reminder message
reminder_message = f"'{task}' is a {priority} priority task."

# Step 3: Process task priority with match case
match priority:
    case "high":
        reminder_message += " That requires immediate attention today!"
    case "medium":
        reminder_message += " Consider completing it soon."
    case "low":
        reminder_message += " Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level entered."

# Step 4: Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"

# Step 5: Print the customized reminder with "Reminder:" prefix
print(f"Reminder: {reminder_message}")
