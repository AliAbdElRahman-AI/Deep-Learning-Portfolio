# ---------------------------------------------------------
# Project: Python Mastery - Control Flow & Membership
# Topics: if, elif, else, Nested If, Ternary Operator, Membership
# Reference: Elzero Web School (Videos 41-45)
# Learner: Ali Abd Ul Rahman
# ---------------------------------------------------------

# 1. Membership Operators (Checking permissions)
allowed_users = ["Ali", "Ramadan", "Mohamed", "Ahmed"] #
user_input = input("Enter your name to login: ").strip().capitalize() #

if user_input in allowed_users: #
    print(f"Access Granted! Welcome {user_input}.")
    
    # 2. Nested If (Deep Learning Project Access)
    project_ready = input("Is the 'A.L.I' project ready? (yes/no): ").lower() #
    if project_ready == "yes":
        print("Starting Project A.L.I presentation...")
    else:
        print("Please complete the project first.")
        
else:
    print("Access Denied. You are not in the allowed users list.") #

# 3. Ternary Conditional Operator (Quick Status Check)
# Shortcut for: Result if Condition else Alternative
user_age = int(input("Enter your age: ")) #
status = "Professional" if user_age > 20 else "Student" #
print(f"User Category: {status}")

# 4. Advanced Age Calculator Logic (Small Sample)
#
months = user_age * 12
print(f"You have lived for {months} months.")
