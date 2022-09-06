for i in range(1, 10):
  if (i % 3) == 0:
    break
  print(i)
else:
  print('---- loop ended ----')

# ==============================================

for i in range(1, 10):
  if i > 3:
    break
  for j in range(1, 10):
    if j > 5:
      break
    print(i * j, end=' ')
  print()
