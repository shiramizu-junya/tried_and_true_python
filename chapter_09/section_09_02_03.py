class BodyType():
  pass

taro = BodyType()
taro.height = 170
taro.weight = 63.5
print(taro, taro.height, taro.weight)
# => <__main__.BodyType object at 0x10a407820> 170 63.5

# ==============================================

hanako = BodyType()
print(hanako.height, hanako.weight)
# => AttributeError: 'BodyType' object has no attribute 'height'

hanako.height = 160
hanako.weight = 48
print(hanako.height, hanako.weight)  # => 160 48

