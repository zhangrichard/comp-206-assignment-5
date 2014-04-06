#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb,re


def template():
	print "Content-type:text/html\r\n\r\n"
	try : 
		f=open("./html/createsurvey.html","r")
		f1=open("survey.ssv","r")
		lines = f.readlines()
		title = f1.readline()
			 #  if find the title Tag <textarea rows="4" cols="50" name="title" placeholder="Enter your title here ..."></textarea>
		for line in lines :    
			 titleTag = '.*name="title".*'
			 if re.search (titleTag,line) :
			 	line = '<textarea rows="4" cols="50" name="title">'+title+'</textarea>'
			 if re.search ("../.*.py",line) :
			 	line = re.sub("../",'./',line)
			 print line

		f.close()
	except IOError:
		print"cannot open file"
