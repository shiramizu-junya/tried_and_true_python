class BodyType:
  def __init__(self, height = 0, weight = 0, name = '太郎'):
    self.height = height
    self.weight = weight
    self.__name = name

  def get_name(self):
    return self.__name

  def __bmi_calc(self):
    h = self.height * 0.01
    bmi = self.weight / (h**2)
    return round(bmi, 1)

  def bmi_hantei(self):
    bmi = self.__bmi_calc()

    if bmi < 18.5:
      return bmi, '低体重'
    elif bmi < 25.0:
      return bmi, '普通体重'
    elif bmi < 35.0:
      return bmi, '肥満'
    else:
      return bmi, '高度肥満'

taro = BodyType(170, 63.5, '佐藤')

print(taro.bmi_hantei()) # => (22.0, '普通体重')

# print(taro.__bmi_calc())
# => AttributeError: 'BodyType' object has no attribute '__bmi_calc'

print(taro.height)  # => 170

print(taro.get_name())  # => 佐藤

print(taro.__name)
# => AttributeError: 'BodyType' object has no attribute '__name'

# ==============================================
