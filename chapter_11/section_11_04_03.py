import csv

fruits = {
  'apple': 200,
  'orage': 250,
  'banana': 300,
  'mango': 2000,
  'strawberry': 200
  }

with open('fruits.csv', 'w', newline='') as f:
  fwriter = csv.writer(f, delimiter=',')
  for item in fruits.items():
    fwriter.writerow(item)

# ==============================================
