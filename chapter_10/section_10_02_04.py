colors = ['red', 'green', 'blue']

try:
  for i in range(5):
    print(colors[i])
except Exception as err:
  print(type(err), err)  # => <class 'IndexError'> list index out of range

print('--- END ---')

# ==============================================

try:
  key = int(input('値を入力 → ')) # => a
  print(key)
except Exception as err:
  print(type(err), err)
  # => <class 'ValueError'> invalid literal for int() with base 10: 'a'
