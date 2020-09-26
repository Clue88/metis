#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb
cgitb.enable()

from datetime import date, datetime, timezone, timedelta
from planner_date import format_date

hw_path = 'hw.csv'

Template = '''
<html><head><script>window.location.href="index.py"</script></head></html>
'''

def main():
    form = cgi.FieldStorage()
    HTML = Template

    id = form.getvalue('id')

    f = open(hw_path, 'r')
    hw = f.read()
    f.close()
    
    subject = form.getvalue('class') or 'N/A'
    assignment = form.getvalue('assignment') or 'N/A'
    due = format_date(form.getvalue('due')) or '2020-01-01'
    submit = form.getvalue('submit') or 'N/A'
    link = form.getvalue('link') or ''

    rows = hw.split('\n')[0:-1]
    new_hw = ''
    for row in rows:
        if row.split('\t')[0] == id:
            new_row = '\t'.join([id, subject, assignment, due, submit, link, 'False'])
            new_hw += new_row + '\n'
        else:
            new_hw += row + '\n'

    f = open(hw_path, 'w')
    f.write(new_hw)
    f.close()

    print(HTML)

main()
