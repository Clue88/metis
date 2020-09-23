#! /usr/bin/python
print ('Content-type: text/html\n')

import cgi, cgitb
cgitb.enable()

f = open('templates/login.html', 'r')
Template = f.read()
f.close()

def main():
    HTML = Template

    print(HTML)

main()
