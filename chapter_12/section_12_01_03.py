import matplotlib.pyplot as plt

x = []
y = []

for i in range(-3, 4):
  x.append(i)
  y.append(i ** 2)

plt.plot(x, y)
plt.show()

# =======================================
