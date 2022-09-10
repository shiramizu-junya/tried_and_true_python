import csv

with open('score.csv', 'r', newline='') as f:
  for row in csv.reader(f):
    print(row)
# => ['75', '80', '65']
#    ['100', '70', '90']
#    ['60', '50', '100']
#    ['85', '80', '75']
#    ['90', '65', '70']

# ==============================================

d = []

with open('score.csv', 'r', newline='') as f:
  for row in csv.reader(f):
    d.append(list(map(int, row)))

print(d)
# => [[75, 80, 65], [100, 70, 90], [60, 50, 100], [85, 80, 75], [90, 65, 70]]
