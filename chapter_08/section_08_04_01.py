def show_message(nm):
  msg = 'こんにちは' + nm
  print('show_message:' + msg)  # => show_message:こんにちは太郎
  return

name = ('太郎')
show_message(name)

print(msg)
# => NameError: name 'msg' is not defined

# ==============================================

