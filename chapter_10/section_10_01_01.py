a = 100

if a = 100:  # => SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
  print('等しい')
else:
  print('等しくない')

# ==============================================

cm = int(input('長さをcmで入力 → ')  # => SyntaxError: invalid syntax. Perhaps you forgot a comma?
m = cm * 0.01
print(m)

# ==============================================

for i in range(10):
print(i)
# => IndentationError: expected an indented block after 'for' statement on line 1
