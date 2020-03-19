import datetime

today = datetime.date.today()
# print(today)

# print(today.weekday())
# print(today.isoweekday())

# lets calculate a duration of 7 days using timedelta
tdelta = datetime.timedelta(days=7)

# you can add or subtract time delta
# print(today - tdelta)

# diff between two dates is timedelta
bday = datetime.date(2020, 9, 12)
till_bday = bday - today
print(till_bday)

# this was about dates, 
# now lets talk about time


t1 = datetime.datetime(2020, 11, 22, 9, 30, 45, 100000)
# print(t1.date())
# print(t1.time())
# print(t1.year)
# print(t1.month)

tdelta = datetime.timedelta(hours=2)
# print(t1 + tdelta)

# constructor with datetime

t11 = datetime.datetime.today()
t12 = datetime.datetime.now()
t13 = datetime.datetime.utcnow()

# print(t11)
# print(t12)
# print(t13)

# using pytz for time zone information
import pytz

# timezone aware UTC

# dt = datetime.datetime(2020, 1, 22, 9, 45, 59, 100000, tzinfo=pytz.UTC)

# print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

my_timezone = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))

print(my_timezone)

# for tz in pytz.all_timezones:
# 	print(tz)

dt_kol = datetime.datetime.now(tz = pytz.timezone('Asia/Kolkata'))

# convert the date to string format
print(dt_kol.strftime('%B %d, %Y'))

# convert string to date
str_dt = 'July 26, 2012'

dt = datetime.datetime.strptime(str_dt, '%B %d, %Y')
print(dt)

