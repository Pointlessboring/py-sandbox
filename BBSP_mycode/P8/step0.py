# Step 0: Dabbling with datetime basics
# https://docs.python.org/3/library/datetime.html
#
from datetime import date, datetime, timedelta

my_date = date.today()
print(f"Today is: {date.strftime(my_date, '%A %B %d, %Y')}")

# Build string of weekdays starting Sunday
dow = [date.strftime((date.today() + timedelta(d - date.isoweekday(date.today()))) ,"%A") for d in range (7)]
print(dow)

# Build string of months
moy = [date.strftime( date(1,m+1,1) ,"%B") for m in range (12)]
print(moy)
