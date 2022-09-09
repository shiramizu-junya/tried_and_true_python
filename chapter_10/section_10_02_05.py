height = input('身長を入力(cm) → ')
weight = input('体重を入力(kg) → ')

try:
  height = float(height) * 0.01
  weight = float(weight)
  bmi = round(weight / (height ** 2), 1)
  print('BMI →', bmi)
except ValueError:
  print('不正な値を入力しました')
except ZeroDivisionError:
  print('0で割り算できません')
except Exception as err:
  print('その他の例外発生')
  print(err)

# ==============================================
