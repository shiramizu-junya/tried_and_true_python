from unittest import result


class BodyType:
  def __init__(self, height = 0, weight = 0):
    self.height = height
    self.weight = weight

  def bmi_calc(self):
    h = self.height * 0.01
    bmi = self.weight / (h**2)
    return round(bmi, 1)

  def bmi_hantei(self, bmi):
    if bmi < 18.5:
      return '低体重'
    elif bmi < 25.0:
      return '普通体重'
    elif bmi < 35.0:
      return '肥満'
    else:
      return '高度肥満'

taro = BodyType(170, 63.5)
result = taro.bmi_calc() # => 22.0
print(taro.bmi_hantei(result))  # => 普通体重

# ==============================================
