import matplotlib.pyplot as plt
import numpy as np


# uppgift 1:
# ----------


# a
def f(x, y):
    """Helper method to calculate value"""
    return x**2 + y**2


def create_array(x, y):
    # Through list-comprehension the value is calculated
    np_arr = np.array([[f(i, j) for j in range(x)] for i in range(y)])
    return np_arr


NP_A = create_array(8, 10)

# b
# Use step==3, both on row and column to get the values asked for
print(NP_A[2:6:3, 1:5:3])

# c
# Make array one dimensional through flatten()
NP_A_FLAT = NP_A.flatten()
print(NP_A_FLAT)
[print(val) for val in NP_A_FLAT if val > 20 and val < 50]

# d
# Axis == 1 is row
sums = np.min(NP_A, axis=1) + np.max(NP_A, axis=1)
print(sums)

# e
# Where values in NP_A is more than 107, replace it with -100
NP_A_MOD = np.where(NP_A > 107, -100, NP_A)
print(NP_A_MOD)

# f


def create_array_for_f():
    # Create the values in one array
    values = np.array([0, 1, 4, 112, 16, 25, 36, 112, 64, 81])
    # And use repeat to repeat them five times
    sequence = np.repeat(values, 5)
    return sequence


NP_Arr = create_array_for_f()
print(NP_Arr)


# g
def plot_array(arr):
    plt.title("Graf över polynom")
    plt.xlabel("Polynomvärden")
    plt.ylabel("Polynomvärden")
    plt.grid()
    values = arr**2 + 10 * arr + 5
    plt.plot(values)

    plt.show()


plot_array(NP_Arr)
