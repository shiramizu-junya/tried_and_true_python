class BodyType:
  def __init__(self, height = 0, weight = 0):
    self.height = height
    self.weight = weight

taro = BodyType(170, 63.5)
print(taro, taro.height, taro.weight)
# => <__main__.BodyType object at 0x10a635ae0> 170 63.5

hanako = BodyType()
print(hanako, hanako.height, hanako.weight)
# => <__main__.BodyType object at 0x10a635a80> 0 0

hanako.height = 160
hanako.weight = 48
print(hanako, hanako.height, hanako.weight)
# => <__main__.BodyType object at 0x10a635a80> 160 48

# ==============================================

