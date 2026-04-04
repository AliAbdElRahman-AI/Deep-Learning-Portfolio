# ---------------------------------------------------------
# Project: AI Image Dataset Management
# Goal: Mastering Python Lists for Data Organization
# Instructor: Elzero Web School (Videos 21-26)
# ---------------------------------------------------------

# 1. Creating the initial Dataset (List of categories)
dataset_categories = ["CARS", "PLANES", "TRUCKS"]

# 2. Adding new labels (Append & Insert)
dataset_categories.append("BIKES")          # Adding at the end
dataset_categories.insert(0, "SHIPS")        # Adding at the beginning

# 3. Refining the Dataset (Slicing & Sorting)
dataset_categories.sort()                   # Sorting alphabetically
final_count = len(dataset_categories)        # Getting size of dataset

# 4. Displaying Professional Report
print("-" * 40)
print(f"Dataset Status: ACTIVE")
print(f"Total Categories: {final_count}")
print(f"Categories List: {dataset_categories}")
print("-" * 40)

# 5. Accessing Specific Data (Indexing)
first_label = dataset_categories[0]
last_label = dataset_categories[-1]

print(f"Priority Label: {first_label}")
print(f"Last Label: {last_label}")
print("-" * 40)
