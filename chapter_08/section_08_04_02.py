def show_message_2():
  msg = 'こんにちは' + name
  print('show_message:' + msg)  # => show_message:こんにちは太郎
  return

name = '太郎'
show_message_2()

# ==============================================

TAX = 0.1

def calc_hontai(price):
  hontai = price / (1 + TAX)
  hasuu = hontai - int(hontai)

  if hasuu > 0:
    result = int(hontai) + 1
  else:
    result = int(hontai)

  return result

hontai = calc_hontai(3000)
print(hontai)
