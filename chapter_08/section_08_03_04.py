def average(*args):
  print(args)  # => (1, 2, 3) tuple型
  return

average(1, 2, 3)

# ==============================================

def average(*args):
  goukei = 0
  for x in args:
    goukei += x
  ave = goukei / len(args)
  return ave

answer = average(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(answer)  # => 5.0

answer = average(1, 2, 3, 4, 5)
print(answer)  # => 3.0

# ==============================================

def func(a, b, *args):
  print(a, b, args)  # => 1 2 (3, 10, 20)

func(1, 2, 3, 10, 20)

# ==============================================

def func(*args, a, b):
  print(a, b, args)

func(1, 2, 3, 10, 20)
# => TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'

func(1, 2, 3, a=10, b=20)  # => 10 20 (1, 2, 3)

# ==============================================

def func(**kwargs):
  print(kwargs)  # => {'a': 1, 'b': 2, 'c': 3} dict(辞書)型
  print(kwargs['a'])  # => 1
  return

func(a = 1, b = 2, c = 3)
