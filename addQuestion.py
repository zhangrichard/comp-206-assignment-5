#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, createSurvey

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

question  = form.getvalue('question')

try : 
	f=open("survey.ssv","a")
	f.write(str(question)+"\n")

	f.close()
except IOError:
	print"cannot open file"


createSurvey.template()