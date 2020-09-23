#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb, hashlib
cgitb.enable()

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

    rows = tests.split('\n')[0:-1]
    new_test = ''
    for row in rows:
        if row.split('\t')[0] == id:
            new_row = row.replace('False', 'True')
            new_test += new_row + '\n'
        else:
            new_test += row + '\n'

    f = open(test_path, 'w')
    f.write(new_test)
    f.close()

    print(HTML)

main()
