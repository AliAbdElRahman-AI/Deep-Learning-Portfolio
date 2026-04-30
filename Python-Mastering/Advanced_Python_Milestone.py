# ---------------------------------------------------------
# Project: Advanced Python Logic & File Management
# Milestone: Completion of 85 Fundamental Lessons
# Role: AI Engineer (Machine Learning Specialization)
# Concepts: Functions, Loops, File I/O, Error Handling
# ---------------------------------------------------------

import os

def process_engineering_data(data_list):
    """
    Function to filter and process scientific data.
    Demonstrates: Functions, Membership, and List Manipulation.
    """
    processed_results = []
    
    # Professional Filtering Logic
    for item in data_list:
        if isinstance(item, (int, float)):
            # Normalize data (Example: Simple feature scaling logic)
            processed_results.append(item * 1.5)
        elif isinstance(item, str) and item.startswith("AI_"):
            processed_results.append(item.upper())
            
    return processed_results

def save_report(content, filename="Engineering_Report.txt"):
    """
    Function to handle file operations.
    Demonstrates: File Handling (Lesson 79-85).
    """
    try:
        with open(filename, "w") as file:
            file.write("--- Python Mastery Report ---\n")
            for line in content:
                file.write(f"Record: {line}\n")
        print(f"Success: Report saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

# --- Main Execution Block ---
if __name__ == "__main__":
    # 1. Raw Data Input (Mixed Types)
    raw_data = [10, "AI_Model_V1", 25.5, "AI_Research", 40, "Invalid_Data"]
    
    print("Starting Data Processing Pipeline...")
    
    # 2. Process Data using the Function
    clean_data = process_engineering_data(raw_data)
    
    # 3. Iterating with Loops (Lesson 47-55)
    for entry in clean_data:
        status = "Numeric" if isinstance(entry, (int, float)) else "System-Label"
        print(f"Processed: {entry} | Category: {status}")

    # 4. Save Final Results to File (Lesson 79-85)
    save_report(clean_data)

    print("-" * 30)
    print("Milestone reached: 85 Lessons Applied Successfully.")
