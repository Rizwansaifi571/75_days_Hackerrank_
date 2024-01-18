# Date : 18,Jan,2024

'''
Calendar Module
The calendar module allows you to output calendars and provides additional
useful functions for them.

class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.

Task:
You are given a date. Your task is to find what the day is on that date.
'''

import calendar
date = list(map(int, input('Enter :').split()))
weekday_index = calendar.weekday(date[2], date[0], date[1])
weekday_name = calendar.day_name[weekday_index]
print(weekday_index)
print(weekday_name.upper())


'''return whole calendar'''
import calendar
print (calendar.TextCalendar(firstweekday=6).formatyear(2015))