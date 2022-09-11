def division(a, b):
  # 割り算の商と余り
  shou = a // b
  amari = a % b
  return shou, amari

def average(*args):
  # 平均を求める
  goukei = 0
  for x in args:
    goukei += x
  ave = goukei / len(args)
  return ave
