#!C:\Users\honsyacl41\Anaconda3\python.exe
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()
import cgi
print("Content-Type: text/html\n")
print("Hello World")
print("<html><body>")
form = cgi.FieldStorage()
form_check = 0
print(form)
if 'name' in form and 'mail' in form :
    form_check = 1
if form_check == 0 :
    print("<h1>ERROR !</h1>")
else :
    print("<h2>PRINT</h2><hr>")
    print("<b>name: </b>", form["name"].value)
    print("<b>mail: </b>", form["mail"].value)
print("</body></html>")
