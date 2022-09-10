with open('score.csv') as f:
  print(f)  # => <_io.TextIOWrapper name='score.csv' mode='r' encoding='UTF-8'>

# ==============================================

with open('hello.txt', 'w') as f:
  f.write('おはよう\nこんにちは\nこんばんは')
  f.write('文章を追加')

# ==============================================

with open('hello.txt', 'r') as f:
  date = f.read()
print(date)

