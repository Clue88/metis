#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb, hashlib
cgitb.enable()

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

    rows = hw.split('\n')[0:-1]
    new_hw = ''
    for row in rows:
        if row.split('\t')[0] == id:
            new_row = row.replace('False', 'True')
            new_hw += new_row + '\n'
        else:
            new_hw += row + '\n'

    f = open(hw_path, 'w')
    f.write(new_hw)
    f.close()

    print(HTML)

main()
