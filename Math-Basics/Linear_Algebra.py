import numpy as np

# 🧠 Linear Algebra Foundations for AI
# This script covers essential matrix operations used in Neural Networks

# 1. Defining Vectors and Matrices (Tensors)
vector = np.array([1, 2, 3])
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# 2. Matrix Multiplication (Dot Product)
# This is how weights are applied in Deep Learning
dot_product = np.dot(matrix_a, matrix_b)

# 3. Matrix Transpose
# Essential for backpropagation
transpose = matrix_a.T

# 4. Determinant and Inverse
det = np.linalg.det(matrix_a)

print("Matrix Multiplication Result:\n", dot_product)
print("Transpose of Matrix A:\n", transpose)
