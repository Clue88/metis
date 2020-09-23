#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb
cgitb.enable()

from datetime import date, datetime, timezone, timedelta
from planner_date import unformat_date

test_path = 'tests.csv'

f = open('templates/edit_test.html', 'r')
Template = f.read()
f.close()

def main():
    form = cgi.FieldStorage()
    HTML = Template

    id = form.getvalue('id')

    f = open(test_path, 'r')
    tests = f.read()
    f.close()

    old_class = 'N/A'
    old_test = 'N/A'
    old_due = '2020-01-01'
    for row in tests.split('\n')[0:-1]:
        if row.split('\t')[0] == id:
            old_class = row.split('\t')[1]
            old_test = row.split('\t')[2]
            old_due = unformat_date(row.split('\t')[3])

    f = open('classes.csv', 'r')
    classes_list = f.read()
    f.close()

    classes = ''
    for _class in classes_list.split('\n')[0:-1]:
        if _class == old_class:
            classes += '<option selected>' + _class + '</option>'
        else:
            classes += '<option>' + _class + '</option>'

    HTML = HTML.replace('// classes //', classes)
    HTML = HTML.replace('// old_test //', old_test)
    HTML = HTML.replace('// old_due //', old_due)
    HTML = HTML.replace('// id //', id)

    print(HTML)

main()
