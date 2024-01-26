# Practice tasks from "Ingenjörens guide till Python"

import numpy as np

# 5.1
# a
int_array = np.array(np.arange(1, 4), int)
print(int_array)

# b
float_array = np.array(np.arange(1, 8), float)
print(float_array)

# 5.2
# a
int_array = np.array([[1], [2], [3], [4]], int)
print(int_array)

# b
float_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(float_array)


# 5.3
b = np.array([[1, 2, 3], [4, 5, 6]], float)
print(f"Array shape  = {b.shape}")
print(f"Array ndim  = {b.ndim}")
print(f"Array dtype  = {b.dtype}")
print(f"Array size  = {b.size}")
print(f"Array itemsize  = {b.itemsize}")


# 5.4
a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], float)
print(a)
b = a.reshape(-1)
print(b)


# 5.5
a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(a)
b = np.resize(a, [12, 12])
print(b)

# 5.6
new_array_float = np.zeros([5, 5], float)
print(new_array_float)

# 5.7
new_array_int = np.ones([10, 10], int)
print(new_array_int)

# 5.8
new_array_with_value = np.ones([10, 5], int) * 27
print(new_array_with_value)

# 5.9
arange_array = np.arange(10, 110).reshape([20, 5])
print(arange_array)

# 5.10
horizontal_array = np.identity(6)
print(horizontal_array)

# 5.11
pi_array = np.linspace(-np.pi, np.pi, 100)
print(pi_array)

# 5.12
array_a = np.arange(25).reshape([5, 5])
print(array_a)
array_b = np.sin(array_a) * 3 + 3.0
print(array_b)

# 5.13
array_a = np.random.randint(0, 100, [5, 5])
array_b = np.random.randint(0, 100, [5, 5])
print(array_a)
print(array_b)
array_c = array_a @ array_b
print(array_c)

# 5.14
arr = np.arange(36).reshape([6, 6])
print(arr)
# a
print(
    arr[
        1,
        :1,
    ]
)

# b
print(arr[2, :])

# c
print(arr[:, 3])

# d
print(arr[-1, :])

# e
print(arr[:, -1])

# f
print(arr[-2, :])
