# Practice tasks from "Ingenjörens guide till Python"

# 3.1
i = 47

# 3.2
x = 67.5

# 3.3
name = "Python is fun"

# 3.4
a = 42.0
print(f"The variable a has the value {a}")

# 3.5
l = [4, 6, 32]

# 3.6
# Is the variable name 56tal valid?
# No

# 3.7
flag = True

# 3.8
l = [5, 6, 7, 37, "s"]
print(l)
l[2] = 42
print(l)

# 3.9
l = ["a", 2, 7, 3.0, 4.5]
print(l[-1])

# 3.10
empty_list = []

# 3.11
l = [1, 2, 3, 4, 5, 6, 7]
l2 = l[1:]
print(l2)

# 3.12
l = [67, 87, 34, 67, 99]
l2 = l[1 : len(l) - 1]
print(l2)

# 3.13
l = [67, 87, 34, 67, 99]
l.append(100)
print(l)

# 3.14
l = [67, 87, 34, 67, 99]
l.insert(0, 52)
print(l)

# 3.15
l = [67, 87, 34, 67, 99]
l.insert(2, -27)
print(l)

# 3.16
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
l.remove("Per")
print(l)

# 3.17
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
del l[l.index("Sven")]
print(l)

# 3.18
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
del l[3:]
print(l)

# 3.19
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
del l[:2]
print(l)

# 3.20
rows, columns = 5, 6
l = [[42 for x in range(columns)] for y in range(rows)]
print(l)

matrix = []
matrix.append([42] * 6)
matrix.append([42] * 6)
matrix.append([42] * 6)
matrix.append([42] * 6)
matrix.append([42] * 6)
print(matrix)

# 3.21
phone_book = {"Arne": 47329823, "Bengt": 91238129, "Stina": 1928319, "Lena": 98129312}
print(phone_book)

# 3.22
if "Stina" in phone_book:
    print(f"Stina is found in {phone_book}")

# 3.23
# Parenthesis is missing

# 3.24
for i in range(2, 10, 3):
    print(i)

# 3.25
l = [45, 78, 90, 34, 23]
for i in l:
    print(i)

# 3.26
l = [45, 78, 90, 34, 23]
for i in range(len(l)):
    print(i)

# 3.27
l = [45, 78, 90, 34, 23]
for i in range(0, len(l), 2):
    print(l[i])

# 3.28
a = [3, 6, 7, 10, 34, 32]
b = [76, 45, 10, 6, 89, 11]
c = [val1 * val2 for val1, val2 in zip(a, b)]
print(c)

# 3.29
nested_list = [[1, 2, 3], [4, 5, 6, 7, 8, 9], [10, 11]]
for sub_list in nested_list:
    for val in sub_list:
        print(val)

# 3.30
sum = 0.0
n = 1
diff = 1e16

while diff > 1e-16:
    last_sum = sum
    sum += 1 / (pow(3, n))
    diff = sum - last_sum
    n += 1
    print("Iteration", n, "sum = ", sum, "diff = ", diff)

# 3.31
import math

for n in range(2, 100):
    prime = True
    k = 2
    while k <= math.sqrt(n) and prime:
        if n % k == 0:
            prime = False
            break
        k += 1
    if prime:
        print("n =", n, "är ett primtal.")


# 3.32
import math


def is_n_a_prime(n: int):
    k = 2
    while k <= math.sqrt(n):
        if n % k == 0:
            return False
        k += 1
    print("n =", n, "är ett primtal.")
    return True


for n in range(2, 100):
    is_n_a_prime(n)


# 3.33
from random import randint


def change_negative_values_to_zero(val_list: list):
    for i in range(len(val_list)):
        if val_list[i] < 0:
            val_list[i] = 0


val_list = [randint(-100, 101) for i in range(100)]
print(val_list)
change_negative_values_to_zero(val_list)
print(val_list)


# 3.34
def f(x):
    return x**3 - x - 1


def deriv_f(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h


if __name__ == "__main__":
    print("fprim(1.0) =", deriv_f(f, 1.0))


# 3.35
import math


def f(x):
    return math.sin(x)


def print_values_table(start: int, stop: int, step: int, f):
    print("{x_label:^10}{y_label:^10}".format(x_label="x", y_label="f(x)"))

    x = start
    while x <= stop:
        print("{x:<10.4f} {f:<10.4f}".format(x=x, f=f(x)))
        x += step


if __name__ == "__main__":
    print_values_table(-2 * math.pi, 2 * math.pi, 0.1, f)


# 3.36
def save_to_file(val_list: list):
    try:
        with open("data/list.csv", "w") as file:
            for row in val_list:
                val_row = ""
                for val in row:
                    val_row += str(val) + " "
                file.write(val_row.strip() + "\n")
    except FileNotFoundError as e:
        print(f"The file or folder does not exist! \n {e}")


if __name__ == "__main__":
    val_list = [[45, 78, 56, 34], [9, 23, 23], [34, 87], [12, 19, 78, 56, 45]]
    save_to_file(val_list)


# 3.37
def read_file_to_list() -> list:
    values = []
    with open("data/list.csv", "r") as file:
        lines = file.readlines()
    for line in lines:
        values.append([int(val) for val in line.split()])
    return values


if __name__ == "__main__":
    values_list = read_file_to_list()
    print(values_list)


# 3.38
def read_data(file_name: str) -> [list, list]:
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"The file or folder ({file_name}) does not exist!")
    table = []
    try:
        for line in lines[1:]:
            temp_line = line.split(",")
            index = int(temp_line[0])
            erupt_length = float(temp_line[1])
            erupt_wait = int(temp_line[2])
            table.append([index, erupt_length, erupt_wait])
    except Exception as e:
        print(f"Unhandled exception occured! \n {e}")

    return lines[0], table


def write_data(header: list, table: list, file_name: str):
    try:
        with open(file_name, "w") as file:
            file.write(header)
            for row in table:
                file.write(", ".join([str(val) for val in row]) + "\n")
    except FileNotFoundError:
        print(f"The file or folder ({file_name}) does not exist!")


def query_data(table: list, max_level: float) -> list:
    new_list = []
    for row in table:
        if row[1] > max_level:
            new_list.append(row)

    return new_list


if __name__ == "__main__":
    header, values = read_data("data/faithful.csv")
    new_values = query_data(values, 4.5)

    file_name = "data/faithful_max_4_5.csv"
    write_data(header, new_values, file_name)
