def strlen(target):
  cnt = 0
  for s in target:
    cnt += 1
  return cnt

n = strlen(123)  # => TypeError: 'int' object is not iterable
print(n)

# ==============================================


def strlen(target):
  if type(target) != str:
    return
  cnt = 0
  for s in target:
    cnt += 1
  return cnt

n = strlen(123)
print(n)  # => None

