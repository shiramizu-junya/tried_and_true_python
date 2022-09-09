class BodyType:
  cnt = 0

  def __init__(self, height=0, weight=0):
    self.height = height
    self.weight = weight
    BodyType.cnt += 1

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

print(BodyType.cnt) # => 0
taro = BodyType(170, 63.5)
print(BodyType.cnt) # => 1
hanako = BodyType(160, 48)
print(BodyType.cnt) # => 2
momoko = BodyType(160, 60)
print(BodyType.cnt) # => 3

# インスタンスからクラス変数を呼び出せる。しかし・・・下に続く
print(taro.cnt)  # => 3
print(hanako.cnt)  # => 3

# クラス変数と同じ名前のインスタンス変数を作ると、インスタンス変数を参照する
taro.cnt = 100
print(taro.cnt)  # => 100

# クラス変数はクラスの外からでも値を変更できる
BodyType.cnt = 10
print(BodyType.cnt) # => 10

# ==============================================
