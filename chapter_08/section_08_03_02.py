def substr(strs, pos, n):
  s = pos - 1
  e = s + n
  return strs[s:e]


s = substr('pineapple', 5, 3)
print(s)  # => app

# s = substr(5, 3, 'pineapple')
# => TypeError: unsupported operand type(s) for +: 'int' and 'str'

s = substr(pos = 5, n = 3, strs = 'pineapple')
print(s)  # => app

s = substr(p = 5, n = 3, strs = 'pineapple')
# => TypeError: substr() got an unexpected keyword argument 'p'

s = substr('pineapple', pos = 5, n = 3)
print(s)  # => app

s = substr(pos = 5, n = 3, 'pineapple')
# => SyntaxError: positional argument follows keyword argument

# ==============================================
