#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb,createSurvey

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

title  = form.getvalue('title')
name = form.has_key("title")

try : 
	f=open("survey.ssv","w")
	f.write(str(title)+"\n")
	f.write(str(name)+"\n")
	f.close()
except IOError:
	print"cannot open file"

createSurvey.template()



# #!/usr/bin/python

# # Import modules for CGI handling 
# import cgi, cgitb 

# # Create instance of FieldStorage 
# form = cgi.FieldStorage() 

# # Get data from fields
# title = form.getvalue('title')

# try : 
# 	f=open("survey.ssv","a")
# 	f.write(str(title))
# 	f.close()
# except IOError:
# 	print"cannot open file"