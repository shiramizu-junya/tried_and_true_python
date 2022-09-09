def strlen(target):
  cnt = 0
  for s in target:
    cnt += 1
  return cnt

n = strlen('blueberry')
print(n)
# => 9

# ==============================================

def say_hello(name):
  print('Hello' + name)

say_hello('太郎')  # => Hello太郎

# ==============================================

say_goodbye('太郎')  # => NameError: name 'say_goodbye' is not defined

def say_goodbye(name):
  print('Goodbye' + name)

# ==============================================

