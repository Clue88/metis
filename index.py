#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb
cgitb.enable()

from datetime import date, datetime, timezone, timedelta

from schedules import get_schedule
from tables import get_hw, get_tests

f = open('templates/index.html', 'r')
Template = f.read()
f.close()

schedule_path = 'schedules.csv'

username = "Christopher"

def main():
    HTML = Template

    # Username
    HTML = HTML.replace('// username //', username)

    # Today's Date
    today = datetime.now(tz=timezone(timedelta(hours=-4), 'US East'))
    format_today = today.strftime('%A, %B %-d, %Y')
    HTML = HTML.replace('// date //', str(format_today))

    # Today's Day
    f = open(schedule_path, 'r')
    schedules = f.read()
    f.close()

    date = today.strftime('%-m/%-d/%-y')
    day_letter = None
    day_periods = None
    for row in schedules.split('\n'):
        if row.split(',')[0] == date:
            day_letter = row.split(',')[1]
            day_periods = row.split(',')[2]
            break
        
    if day_letter is not None and day_periods is not None:
        day = 'Day ' + day_letter + ' (' + day_periods + ')'
    else:
        day = 'No school today!'

    table_schedule = get_schedule(day_letter, day_periods)
    HTML = HTML.replace('// day //', day)

    # Tables
    table_hw = get_hw()
    table_tests = get_tests()
    
    HTML = HTML.replace('// table_schedule //', table_schedule)
    HTML = HTML.replace('// table_hw //', table_hw)
    HTML = HTML.replace('// table_tests //', table_tests)

    print(HTML)

main()
