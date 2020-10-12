#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb
cgitb.enable()

from datetime import date, datetime, timezone, timedelta
from planner_date import format_date

test_path = 'tests.csv'

Template = '''
<html><head><script>window.location.href="index.py"</script></head></html>
'''

def main():
    form = cgi.FieldStorage()
    HTML = Template

    id = form.getvalue('id')

    f = open(test_path, 'r')
    tests = f.read()
    f.close()
    
    subject = form.getvalue('class') or 'N/A'
    test = form.getvalue('test') or 'N/A'
    due = form.getvalue('due') or '2022-12-31'
    due = format_date(due)

    rows = tests.split('\n')[0:-1]
    new_test = ''
    for row in rows:
        if row.split('\t')[0] == id:
            new_row = '\t'.join([id, subject, test, due, 'False'])
            new_test += new_row + '\n'
        else:
            new_test += row + '\n'

    f = open(test_path, 'w')
    f.write(new_test)
    f.close()

    print(HTML)

main()
