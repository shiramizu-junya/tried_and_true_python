import datetime

deadline = datetime.date(2022, 12, 10)
dt = datetime.date.today()
diff = deadline - dt
print(diff)  # => 91 days, 0:00:00
diff # => datetime.timedelta(days=91)
type(diff) # => <class 'datetime.timedelta' >

# ==============================================

dt = datetime.date.today()
dt_2 = dt + datetime.timedelta(days=100)
print(dt)  # => 2022-09-10
print(dt_2)  # => 2022-12-19
