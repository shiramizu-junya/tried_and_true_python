fruits = {'apple': 250, 'orange': 200, 'banana': 300}
print(fruits.pop('apple', None))
# => 250
fruits
# => {'orange': 200, 'banana': 300}

# ==============================================

fruits = {'apple': 250, 'orange': 200, 'banana': 300}
print(fruits.pop('mango', None))
# => None
fruits
# => {'apple': 250, 'orange': 200, 'banana': 300}
print(fruits.pop('mango'))
# => KeyError: 'mango'

