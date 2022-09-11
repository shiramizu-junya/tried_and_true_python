import pandas as pd

df = pd.read_csv('score_title.csv')
print(df)
print('=============')
print(df['数学'][1])
print('=============')
print(df['国語'])
