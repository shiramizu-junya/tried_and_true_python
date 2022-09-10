import datetime

2021-3-15 < 2021-5-1 # => True

dt_1 = datetime.date(2021, 3, 15)
dt_2 = datetime.date(2021, 5, 1)
dt_1 < dt_2  # => True

# ==============================================

from datetime import datetime, date

print(date.today())
print(datetime.now())

