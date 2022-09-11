import bmi
from bmi import BodyTypeExtra

taro = bmi.BodyType(170, 63.5)
print(taro.bmi_hantei())

hanako = BodyTypeExtra(160, 48, 30)
print(hanako.ideal_weight())
