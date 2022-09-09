def division(a, b):
  try:
    shou = a // b
    amari = a % b
  except Exception as err:
    print('func:', err)
    shou = None
    amari = None
  return shou, amari

answer = division(10, 0)
print(answer)


# ==============================================
