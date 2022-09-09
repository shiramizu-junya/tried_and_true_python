colors = ['red', 'green', 'blue']

for i in range(5):
  print(colors[i])
  '''
  red
  green
  blue
  IndexError: list index out of range
  '''

print('--- END ---')

# ==============================================

key = int(input('値を入力 → '))
# => ValueError: invalid literal for int() with base 10: '12.5'
print(key)
