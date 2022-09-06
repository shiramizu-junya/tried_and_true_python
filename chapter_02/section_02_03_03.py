# コンピューターとの会話プログラム
name = input('What your name?') # 名前を入力
print('Hello ' + name) # 画面に表示

##################################################

score = int(input('点数を入力'))
if score >= 80:
  print('A')
  '''
  elif score >= 60:
    print('B')
  '''
else:
  print('追試')
