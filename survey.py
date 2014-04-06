#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb,re



print "Content-type:text/html\r\n\r\n"
try : 
	f=open("./html/survey.html","r")
	f1=open("survey.ssv","r")
	lines = f.readlines()
	title = f1.readline()
		 #  if find the title Tag <textarea rows="4" cols="50" name="title" placeholder="Enter your title here ..."></textarea>
	for line in lines :    
		 # titleTag = '.*name="title".*'
		 # question1 = '.*name="title".*'
		 # question2 = '.*name="title".*'
		 # question3 = '.*name="title".*'
		 # question4 = '.*name="title".*'
		 # question5=''
		
		if re.search ("$Survey_Title",line) :
			 	line = re.sub("$Survey_Title",title,line)
		# for 
		print line

	f.close()
except IOError:
	print"cannot open file"