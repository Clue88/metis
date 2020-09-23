import datetime
import calendar

def format_date(date):
    weekday = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    weekday = calendar.day_name[weekday][0:3]
    year = date.split('-')[0][-2:]
    month = date.split('-')[1]
    if int(month) < 10:
        month = month[1:]
    day = date.split('-')[2]
    if int(day) < 10:
        day = day[1:]

    return weekday + ' ' + month + '/' + day + '/' + year

def unformat_date(date):
    date = date[4:]
    month = date.split('/')[0]
    day = date.split('/')[1]
    year = date.split('/')[2]

    if int(month) < 10:
        month = '0' + month
    if int(day) < 10:
        day = '0' + day
    year = '20' + year

    return year + '-' + month + '-' + day
