#!C:\Users\honsyacl41\Anaconda3\python.exe
# -*- coding:utf-8 -*-
import cgi
import MeCab

print 'Content-type: text/html\n'
print """
<!DOCTYPE html>
<html>
<head>
	<title>CGI Script</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="theme.css">
	<script>
	function clearContents(element) {
		element.value = '';
	}
	</script>
</head>
<body>
<h3>CGI Script</h3>
<form method="post" action="mecabbrowser.py">
	<textarea onfocus="clearContents(this);" name="message">文章を入力してください</textarea>
	<input type="submit" name="submit" value="SEND">
</form>
"""

form = cgi.FieldStorage()
message = form.getvalue('message', '')
tagger = MeCab.Tagger()
result = tagger.parse(message)
l = len(unicode(message,'utf-8')) if message else 0

print """
<p>
<strong>入力された文章:</strong><br>
%s<br><br>
<strong>文字数:</strong>%d
</p>
<h3>形態素解析結果:</h3>
""" % (cgi.escape(message),l)

for line in result.split('\n'):
	word,etc = line.split()
	print '<span>'+word+'</span>'+etc+"<br>"
print '</body></html>'