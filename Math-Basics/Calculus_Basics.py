import numpy as np

# 📉 Calculus for AI: Understanding Gradients
# This script demonstrates how to calculate derivatives using numerical methods

def f(x):
    # Example function: f(x) = x^2
    return x**2

def derivative(f, x):
    # Calculating the slope (gradient) at point x
    h = 0.0001
    return (f(x + h) - f(x)) / h

# Calculate gradient at x = 3
x_value = 3
slope = derivative(f, x_value)

print(f"The slope of f(x) at x={x_value} is approximately: {slope}")
# In AI, this slope tells us in which direction to update our model weights!
