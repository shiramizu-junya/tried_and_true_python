def division(a, b):
  shou = a // b
  amari = a % b
  return shou, amari

answer = division(10, 3)
print(answer)  # => (3, 1)
answer[0] # => 3

# ==============================================

shou, amari = division(10, 3)
shou # => 3
amari # => 1
