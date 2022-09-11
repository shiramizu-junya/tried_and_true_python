import pandas as pd

df = pd.read_csv('score_title.csv')
print(df.mean())
print('==========')
print(df.sum())
