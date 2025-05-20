import numpy as np

# 2. Create Arrays:
A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

print("Array A:", A)
print("Array B:", B)

# 3. Perform Operations:
add_result = A + B
subtract_result = A - B
multiply_result = A * B
divide_result = A / B

print("\nAddition (A + B):", add_result)
print("Subtraction (A - B):", subtract_result)
print("Element-wise Multiplication (A * B):", multiply_result)
print("Division (A / B):", divide_result)

# 4. Apply NumPy Functions:
mean_A = np.mean(A)
max_A = np.max(A)
min_A = np.min(A)
dot_product_AB = np.dot(A, B)
A_reshaped = A.reshape(5, 1)

print("\nMean of A:", mean_A)
print("Maximum of A:", max_A)
print("Minimum of A:", min_A)
print("Dot product of A and B:", dot_product_AB)
print("Reshaped A (5x1 matrix):\n", A_reshaped)