import matplotlib.pyplot as plt
import numpy as np

arr = np.array([75, 100, 60, 85, 90])
arr  # => array([ 75, 100,  60,  85,  90])
print(type(arr))  # => <class 'numpy.ndarray'>

# =======================================

arr = np.arange(0, 1, 0.1)
arr  # => array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
