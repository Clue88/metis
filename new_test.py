#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb
cgitb.enable()

f = open('templates/new_test.html', 'r')
Template = f.read()
f.close()

f = open('classes.csv', 'r')
classes_list = f.read()
f.close()

classes = ''
for _class in classes_list.split('\n')[0:-1]:
    classes += '<option>' + _class + '</option>'

def main():
    HTML = Template

    HTML = HTML.replace('// classes //', classes)

    print(HTML)

main()
