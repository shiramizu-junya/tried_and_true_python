import matplotlib.pyplot as plt
import numpy as np

arr = np.array([75, 100, 60, 85, 90])
arr  # => array([ 75, 100,  60,  85,  90])
print(type(arr))  # => <class 'numpy.ndarray'>

# =======================================

arr = np.arange(0, 1, 0.1)
arr  # => array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

# =======================================

list_a = [1, 2, 3]
list_b = []

for dat in list_a:
  list_b.append(dat * 3)

list_b  # => [3, 6, 9]

# =======================================

list_a = [1, 2, 3]
list_b = []

def three_times(val):
  return val * 3

list_b = list(map(three_times, list_a))
list_b  # => [3, 6, 9]

# =======================================

arr = np.array([1, 2, 3])
arr * 3  # => array([3, 6, 9])

# =======================================

list_a = [1, 2, 3]
list_b = [10, 20, 30]

list_a + list_b  # => [1, 2, 3, 10, 20, 30]

# =======================================

arr_a = np.array([1, 2, 3])
arr_b = np.array([10, 20, 30])
arr_a + arr_b  # => array([11, 22, 33])
arr_a * arr_b  # => array([10, 40, 90])

