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
    type(self)._cnt += 1

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
  # クラス変数
  _cnt = 0

taro = BodyTypeExtra(170, 63.5)
print(taro.bmi_hantei())  # => (22.0, '普通体重')

hanako = BodyTypeExtra(160, 48)
print(BodyTypeExtra.count())  # => 2

momoko = BodyType(180, 60)
print(BodyType.count())  # => 1

# ==============================================
