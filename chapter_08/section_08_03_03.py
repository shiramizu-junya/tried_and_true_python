def total_price(price, bag):
  total = price + (bag * 5)
  return total

pay = total_price(2000, 2)
print(pay)  # => 2010

pay = total_price(2000, 0)
print(pay)  # => 2000

# ==============================================

def total_price(price = 0, bag = 0):
  total = price + (bag * 5)
  return total

pay = total_price(2000, 10)
print(pay)  # => 2050

pay = total_price(2000)
print(pay)  # => 2000

# ==============================================

# 必須引数とオプション引数を同時に使う

def total_price(price, bag=0):
  total = price + (bag * 5)
  return total

def total_price(price=0, bag):
  total = price + (bag * 5)
  return total
