# ---------------------------------------------------------
# Project: AI Model Performance Tracker
# Goal: Data Cleaning and Formatting for Model Metrics
# Phase: Python Basics for Data Science
# ---------------------------------------------------------

# 1. Model Metadata (Variables & Numbers)
model_name = "Neural_Net_v1"
training_epochs = 100
initial_accuracy = 0.65234  # Float numbers
final_accuracy = 0.94789    # Float numbers
improvement = final_accuracy - initial_accuracy

# 2. Performance Reporting (Formatting)
# Using formatting to show only 2 decimal places for professionalism
report = "Model: {:s} | Epochs: {:d} | Improvement: {:.2f}%".format(
    model_name, training_epochs, improvement * 100
)

print("-" * 40)
print(">>> AI PERFORMANCE REPORT <<<")
print(report)
print("-" * 40)

# 3. Log Cleaning (String Methods & Slicing)
# Imagine this is a raw log string from a server
raw_log = "   STATUS: active_training_mode_enabled   "

# Cleaning the log to extract only the status
clean_log = raw_log.strip().upper()
status_code = clean_log[8:14] # Extracting "ACTIVE"

print(f"System Log: {clean_log}")
print(f"Current Status: {status_code}")
print("-" * 40)
