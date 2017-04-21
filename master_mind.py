
import cgi
form = cg.FieldStorage()
print form.getvalue("name")