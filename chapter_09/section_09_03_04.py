class BodyType:
  def __init__(self, height = 0, weight = 0):
    self.height = height
    self.weight = weight

  def bmi_calc(self):
    h = self.height * 0.01
    bmi = self.weight / (h**2)
    return round(bmi, 1)

taro = BodyType(170, 63.5)
print(taro.bmi_calc())  # => 22.0

# ==============================================

