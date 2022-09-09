def disp_param(strs, pos, n):
  print('strs:', strs)
  print('pos:', pos)
  print('n:', n)
  return

disp_param('pineapple', 5, 3)
# => strs: pineapple
#    pos: 5
#    n: 3

disp_param('pineapple', 5)
# => TypeError: disp_param() missing 1 required positional argument: 'n'

# ==============================================

def substr(strs, pos, n):
  s = pos - 1
  e = s + n
  return strs[s:e]

s = substr('pineapple', 5, 3)
print(s)  # => app

s = substr(5, 3, 'pineapple')
# => TypeError: unsupported operand type(s) for +: 'int' and 'str'


