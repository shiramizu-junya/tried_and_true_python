def show_message_3():
  name = 'Hanako'
  msg = 'こんにちは、' + name
  print('show_message_3:' + msg)  # => show_message_3:こんにちは、Hanako
  return

name = '太郎'
show_message_3()
print(name)  # => 太郎

# ==============================================

def show_message_4():
  global name
  name = 'Hanako'
  msg = 'こんにちは、' + name
  print('show_message_3:' + msg)  # => show_message_3:こんにちは、Hanako
  return


name = '太郎'
show_message_4()
print(name)  # => Hanako
