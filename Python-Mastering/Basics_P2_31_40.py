# ---------------------------------------------------------
# Project: Python Mastery for Deep Learning (Part 2)
# Topics: Dictionaries, Booleans, Operators, & User Input
# Reference: Elzero Web School (Videos 31-40)
# Learner: Ali Abd Ul Rahman
# ---------------------------------------------------------

# 1. Advanced Dictionary Operations (Model Configuration Example)
model_config = {
    "model_name": "Deep_Neural_Net",
    "layers": 5,
    "activation": "ReLU"
}

# Updating and checking keys
model_config.update({"learning_rate": 0.001})
print(f"Current Config Keys: {model_config.keys()}")
print(f"Activation Function: {model_config.get('activation')}")

# 2. Boolean Logic & Comparison (Data Filtering)
image_size = 224
min_required_size = 200
is_valid_format = True

# Logic: Check if image meets requirements
is_ready_for_training = image_size >= min_required_size and is_valid_format
print(f"Is data ready for Deep Learning? {is_ready_for_training}")

# 3. User Interaction & Data Cleaning
print("-" * 30)
user_full_name = input("Enter your name: ").strip().capitalize()
user_email = input("Enter your email: ").strip().lower()

# Practical Slicing (Extracting Username & Domain)
user_name_slice = user_email[:user_email.index("@")]
domain_slice = user_email[user_email.index("@") + 1:]

print("-" * 30)
print(f"Welcome, Engineer {user_full_name}!")
print(f"Username: {user_name_slice}")
print(f"Domain: {domain_slice}")

# 4. Checking Truthy/Falsy values
# If username is empty, bool() returns False
print(f"Is Name Provided? {bool(user_full_name)}")
