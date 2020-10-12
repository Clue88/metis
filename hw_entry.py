#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb, hashlib
import datetime
import calendar
import uuid
from planner_date import format_date
cgitb.enable()

hw_path = 'hw.csv'

Template = '''
<html><head><script>window.location.href="index.py"</script></head></html>
'''

def main():
    form = cgi.FieldStorage()
    HTML = Template

    id = str(uuid.uuid4().hex)
    subject = form.getvalue('class') or 'N/A'
    assignment = form.getvalue('assignment') or 'N/A'
    due = format_date(form.getvalue('due') or '2022-12-31')
    submit = form.getvalue('submit') or 'N/A'
    link = form.getvalue('link') or ''

    entry = '\t'.join([id, subject, assignment, due, submit, link, 'False']) + '\n'

    f = open(hw_path, 'a')
    f.write(entry)
    f.close()

    print(HTML)

main()
