class BodyType:
  # クラス変数
  _cnt = 0

  # クラスメソッド
  @classmethod
  def count(cls):
    return cls._cnt

  def __init__(self, height=0, weight=0):
    self.height = height
    self.weight = weight
    BodyType._cnt += 1

  def bmi_calc(self):
    h = self.height * 0.01
    bmi = self.weight / (h**2)
    return round(bmi, 1)

  def bmi_hantei(self):
    bmi = self.bmi_calc()

    if bmi < 18.5:
      return bmi, '低体重'
    elif bmi < 25.0:
      return bmi, '普通体重'
    elif bmi < 35.0:
      return bmi, '肥満'
    else:
      return bmi, '高度肥満'

class BodyTypeExtra(BodyType):
  def __init__(self, height, weight, age):
    super().__init__(height, weight)
    self.age = age

  def ideal_weight(self):
    h = self.height * 0.01
    high = round(24.9 * (h ** 2), 1)

    if self.age >= 18 and self.age < 50:
      low = round(18.5 * (h ** 2), 1)
    elif self.age >= 50 and self.age < 65:
      low = round(20.0 * (h ** 2), 1)
    elif self.age >= 65:
      low = round(21.5 * (h ** 2), 1)
    else:
      low = None
      high = None

    return low, high

taro = BodyTypeExtra(170, 63.5, 30)
print(taro.ideal_weight())  # => (53.5, 72.0)

# ==============================================
