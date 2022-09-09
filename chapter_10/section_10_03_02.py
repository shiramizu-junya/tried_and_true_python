def division(a, b):
  try:
    shou = a // b
    amari = a % b
  except Exception as err:
    print('func:', err)
    shou = None
    amari = None
    raise
  return shou, amari

try:
  answer = division(10, 0)
  print(answer)
except Exception as err:
  print('main:', err)


# ==============================================
