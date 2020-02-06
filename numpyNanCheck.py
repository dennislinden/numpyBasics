import numpy as np
a = np.array([1, 0, np.nan, np.inf, 10, 23.2])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness (oneindig):")
print(np.isinf(a))