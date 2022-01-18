import datetime

Current = datetime.datetime.now()

print(Current)
print(Current.year)             # current year
print(Current.strftime("%A"))   # current Day
print(Current.strftime("%B"))   # Current Month