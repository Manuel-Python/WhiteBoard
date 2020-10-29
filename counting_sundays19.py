# How many Sundays fell on the first of the month during the   Q19
# twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import *
# code based on http://www.pybloggers.com/2015/06/project-euler-19-counting-sundays/
year = 1901
month = 1
process_day = date(year,month,1) # start date

counter = 0
while(process_day.year < 2001):
    if(process_day.weekday() == 6):
        counter += 1
    if(month+1 == 13):
        month = 1
        year += 1
    else:
        month += 1
    process_day = date(year,month,1)

print("Number of Sundays is {}".format(counter))