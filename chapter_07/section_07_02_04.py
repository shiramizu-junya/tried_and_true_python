fruits = { 'apple': 250, 'orange': 200, 'banana': 300 }
fruits['grape'] = 1200
fruits

# ==============================================

fruits.update({'apple': 500, 'orange': 400})

fruits.update({'grape': 1200, 'mango': 3000})

# ==============================================

fruits.setdefault('apple', 500)
# => 250
fruits
# => {'apple': 250, 'orange': 200, 'banana': 300}

fruits.setdefault('mango', 3000)
# => 3000
fruits
# => {'apple': 250, 'orange': 200, 'banana': 300, 'mango': 3000}

