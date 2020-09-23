#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb, hashlib
import datetime
import calendar
import uuid
from planner_date import format_date
cgitb.enable()

test_path = 'tests.csv'

Template = '''
<html><head><script>window.location.href="index.py"</script></head></html>
'''

def main():
    form = cgi.FieldStorage()
    HTML = Template

    id = str(uuid.uuid4().hex)
    subject = form.getvalue('class') or 'N/A'
    assignment = form.getvalue('test') or 'N/A'
    due = format_date(form.getvalue('due') or '2020-01-01')

    entry = '\t'.join([id, subject, assignment, due, 'False']) + '\n'

    f = open(test_path, 'a')
    f.write(entry)
    f.close()

    print(HTML)

main()
