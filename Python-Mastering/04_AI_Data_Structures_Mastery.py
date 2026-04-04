# ---------------------------------------------------------
# Project: AI Integrated Data Structures
# Goal: Combining Lists, Tuples, Sets, and Dictionaries
# Instructor: Elzero Web School (Videos 21-40)
# Learner: Ali Abd Ul Rahman (AI Engineer Pathway)
# ---------------------------------------------------------

# 1. Tuples: Fixed Constants (Immutable)
# Coordinates for a bounding box in an image (x, y, width, height)
IMAGE_SHAPE = (1920, 1080)
print(f"Target Image Resolution: {IMAGE_SHAPE}")

# 2. Sets: Unique Labels (No Duplicates)
# Ensuring no redundant class names in our training set
raw_labels = {"Car", "Truck", "Car", "Bike", "Truck", "Pedestrian"}
unique_labels = sorted(raw_labels) 
print(f"Unique Dataset Labels: {unique_labels}")

# 3. Lists: Dynamic Data (Mutable)
# List of image filenames to be processed
image_files = ["img01.jpg", "img02.jpg", "img03.jpg"]
image_files.append("img04.jpg") # Adding new data
print(f"Total Images in Queue: {len(image_files)}")

# 4. Dictionaries: Complex Mapping (Key-Value Pairs)
# Comprehensive info about our AI Model
ai_model_info = {
    "name": "Object_Detector_v2",
    "accuracy": 0.98,
    "framework": "PyTorch",
    "labels": unique_labels,
    "input_resolution": IMAGE_SHAPE
}

# 5. Accessing & Reporting
print("-" * 40)
print(f">>> DEPLOYING MODEL: {ai_model_info['name']} <<<")
print(f"Model Framework: {ai_model_info.get('framework')}")
print(f"Main Target: {ai_model_info['labels'][0]}")
print("-" * 40)
