class BodyType:
  def __init__(self, height, weight):
    self.height = height
    self.weight = weight

taro = BodyType(170, 63.5)
print(taro, taro.height, taro.weight)
# => <__main__.BodyType object at 0x10a634df0> 170 63.5

hanako = BodyType()
# => TypeError: BodyType.__init__() missing 2 required positional arguments: 'height' and 'weight'
print(hanako, hanako.height, hanako.weight)

# ==============================================

