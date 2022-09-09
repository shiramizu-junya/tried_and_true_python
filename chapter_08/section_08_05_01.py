def get_price(item):
  return item[1]

price = get_price(('apple', 250))
print(price)  # => 250

# ==============================================

price = (lambda item: item[1])(('apple', 250))
print(price)  # => 250

name = (lambda n: 'こんにちは' + n)('佐藤')
print(name)  # => こんにちは佐藤

name = (lambda n1, n2, n3: 'こんにちは' + n1 + n2 + n3)('佐藤', '田中', '鈴木')
print(name)  # => こんにちは佐藤田中鈴木

greet = (lambda : 'こんにちは')
print(greet)  # => <function <lambda> at 0x105c7f400>
