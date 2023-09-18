# datetime module

import datetime

# get current date and time

current_datetime = datetime.datetime.now()

# print(current_datetime)


date1 = datetime.datetime(2023, 9, 7)
date2 = datetime.date(2023, 9, 18)

date_difference = current_datetime - date1

print(date_difference)


# print(help(datetime))
# print(dir(datetime))
