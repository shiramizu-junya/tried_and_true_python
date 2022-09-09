fruits = { 'apple': 250, 'orange': 200, 'banana': 300 }
sorted(fruits)  # => ['apple', 'banana', 'orange']

# ==============================================

sorted(fruits.items())
# => [('apple', 250), ('banana', 300), ('orange', 200)]

# ==============================================

def get_price(item):
  print(item)  # => １回目：('apple', 250)、２回目：('orange', 200)、３回目：('banana', 300)
  return item[1]

sorted(fruits.items(), key = get_price)

# ==============================================

sorted(fruits.items(), key=lambda item: item[1])
# => [('orange', 200), ('apple', 250), ('banana', 300)]
