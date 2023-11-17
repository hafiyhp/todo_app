from time import time, gmtime, strftime

def get_formatted_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def get_epoch_time():
    return int(time())

def get_day_of_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[gmtime().tm_wday]

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False