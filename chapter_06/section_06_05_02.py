from tkinter import N
from turtle import color


numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# ===================================

data = []
for i in range(1, 11):
  # print(i)
  if i % 3 == 0:
    data.append(i)

print(data)

# ===================================

numbers = [1, 2, 3, 4, 5]
numbers.extend([6, 7, 8])
# numbers.extend(range(6, 9))
print(numbers)

# ===================================

colors = ['white', 'black']
colors.insert(1, 'gray')
print(colors)

# ===================================

