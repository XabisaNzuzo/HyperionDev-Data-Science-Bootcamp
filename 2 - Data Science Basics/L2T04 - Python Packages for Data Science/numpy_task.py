import numpy as np
import pandas as nd

# Question 1

# np.array((1, 0, 0), (0, 1, 0), (0, 0, 1), dtype = float)
# does not create a 2D array because of the syntax.
# We should use a list of lists to define the elements of the array properly.

# This creates a 2D array (matrix) with 3 rows and 3 columns.
# Each row represents a unit vector along one of the coordinate
# axes (x, y, z).
# The data type is set to 'float'.
np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)

# Question 2

# The difference between np.array([0,0,0]) and np.array([[0,0,0]]) is
# np.array([0,0,0]) is 1 dimensional and
# np.array([[0,0,0]]) is 2 dimensional with 1 row and 3 columns

# Question 3

# 3 by 4 by 4 array
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

solution_1 = arr[1, 0, -1]
solution_2 = arr[0, 2, 0:]
solution_3 = arr[2, 0:]
solution_4 = arr[0:, 1, 0:2]
solution_5 = arr[2, :, -1:-3:-1]
solution_6 = arr[:, -1:-5:-1, 0]
solution_7 = arr[0:3:2, 0:4:3, 0:4:3].flatten().reshape(4, 2)[0:4:3]
solution_8 = arr[1:3, 0:4, 0:4].flatten()[8:24].reshape(4, -1)

# Display results

print(f"Solution 1: {solution_1}")
print(f"Solution 2: {solution_2}")
print(f"Solution 3: \n {solution_3}")
print(f"Solution 4: \n {solution_4}")
print(f"Solution 5: \n {solution_5}")
print(f"Solution 6: \n {solution_6}")
print(f"Solution 7: \n {solution_7}")
print(f"Solution 8: \n {solution_8}")
