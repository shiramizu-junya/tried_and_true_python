scores = [[75, 80, 65],
          [100, 70, 90],
          [60, 50, 100],
          [85, 80, 70],
          [90, 65, 70]]

for row in range(5):
  for col in range(3):
    print(scores[row][col])

print('============================')

total = 0

for i in range(5):
  total += scores[i][0]

average = total / 5

print(average)
