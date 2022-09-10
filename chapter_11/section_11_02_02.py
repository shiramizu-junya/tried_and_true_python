import random

for i in range(5):
  print(random.randint(1, 10))

# ==============================================

# モジュールをインポートしないと、エラーになる
for i in range(5):
  print(random.randint(1, 10))
  # => NameError: name 'random' is not defined

# ==============================================

omikuji = ('大吉', '吉', '中吉', '小吉', '末吉', '凶')
result = random.randint(0, 5)
print(omikuji[result])
