fruits = {'apple': 250, 'orange': 200, 'banana': 300}
fruits.items()
#  => dict_items([('apple', 250), ('orange', 200), ('banana', 300)])

# ==============================================

fruits = {'apple': 250, 'orange': 200, 'banana': 300}
for key, value in fruits.items():
  print(key, value)
# => apple 250
#    orange 200
#    banana 300

# ==============================================

fruits = {'apple': 250, 'orange': 200, 'banana': 300}
list_fruits = list(fruits.items())
list_fruits
# => [('apple', 250), ('orange', 200), ('banana', 300)]
list_fruits[0]
# => ('apple', 250)
list_fruits[0][0]
# => 'apple'

# ==============================================

fruits = {'apple': 250, 'orange': 200, 'banana': 300}
fruits.keys()
# => dict_keys(['apple', 'orange', 'banana'])

type(fruits.keys())
# => <class 'dict_keys'>

list(fruits.keys())[0]
# => 'apple'

# ==============================================

fruits = {'apple': 250, 'orange': 200, 'banana': 300}
fruits.values()
# => dict_values([250, 200, 300])

type(fruits.values())
# => <class 'dict_values'>

list(fruits.values())[0]
# => 250

# ==============================================

figures = {3: 'triangle', 4: 'rectangle', 5: 'pentagon'}
'pentagon' in figures.values()
# => True


