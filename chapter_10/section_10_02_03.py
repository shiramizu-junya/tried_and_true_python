try:
  key = int(input('値を入力 → '))  # => a
  # 値を入力 → a
except:
  print('例外発生！')
  # 例外発生！

print(key)
# => NameError: name 'key' is not defined

# ==============================================

try:
  key = int(input('値を入力 → '))  # 値を入力 → a
except:
  print('例外発生！')  # 例外発生！
else:
  print(key)
