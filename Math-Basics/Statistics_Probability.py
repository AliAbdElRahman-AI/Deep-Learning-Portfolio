import numpy as np

# 📊 Statistics & Probability for AI
# This script calculates essential metrics used for data normalization

# 1. Sample Data (e.g., house prices or pixel values)
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 2. Basic Statistics
mean = np.mean(data)              # Average
variance = np.var(data)            # How spread out the data is
std_deviation = np.std(data)      # Standard Deviation (Essential for AI scaling)

# 3. Probability Example (Simplified)
# Probability of picking a value greater than 50
prob_gt_50 = len(data[data > 50]) / len(data)

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_deviation}")
print(f"Probability of value > 50: {prob_gt_50}")
