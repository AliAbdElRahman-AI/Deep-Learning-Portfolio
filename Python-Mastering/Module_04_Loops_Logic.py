# ---------------------------------------------------------
# Project: Python Mastery - Membership & Control Flow
# Topics: Practical Membership, While Loop, Loop Else
# ---------------------------------------------------------

# 1. Professional Membership Control (Course Access System)
enrolled_courses = ["Python", "Deep Learning", "Data Analysis", "Machine Learning"]

# Prompting user for input with data cleaning
requested_course = input("Enter course name to verify access: ").strip().title()

if requested_course in enrolled_courses:
    print(f"Verified: Access granted to {requested_course}. You may proceed.")
else:
    print(f"Access Denied: {requested_course} is not in your enrollment list.")

print("-" * 30)

# 2. While Loop & Else (Process Automation)
# Simulating a training process for an AI Model
target_epoch = 5
current_epoch = 1

print(f"Process Started... Goal: {target_epoch} Epochs")

while current_epoch <= target_epoch:
    print(f"Executing Epoch {current_epoch}...")
    current_epoch += 1
else:
    # The 'else' block executes when the loop finishes normally
    print("Process Finished: All epochs completed successfully.")

print("-" * 30)

# 3. Simple Iteration Example
# Using while loop for recurring notification
alerts = 3
while alerts > 0:
    print("System Status: Optimal")
    alerts -= 1
