import random

omikuji = ('大吉', '吉', '中吉', '小吉', '末吉', '凶')
random.choice(omikuji)

# ==============================================

from random import choice, randint

omikuji = ('大吉', '吉', '中吉', '小吉', '末吉', '凶')
choice(omikuji)

for i in range(5):
  print(randint(1, 10))
  print(random.randint(1, 10))
  # => NameError: name 'random' is not defined
