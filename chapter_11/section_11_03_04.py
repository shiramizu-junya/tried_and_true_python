import datetime

dt = datetime.datetime.now()
str_dt = dt.strftime('%Y年%m月%d日（%A）')
str_dt # => '2022年09月10日（Saturday）'
print(str_dt)  # => 2022年09月10日（Saturday）

# ==============================================
