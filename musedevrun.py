# Below script reads project details from projectdetails.txt file which has project name and git link 
#separated by a space in each line. Below python code reads each line, and runs musedev on each project.

import os
import sys
import subprocess

f = open("projectdetails.txt","r")
project_info = f.read().split('\n')
for line in project_info:
	project = line.split()
	projectname = project[0]
	gitlink = project[1]
	subprocess.call(["rm","-rf", projectname])
	dirname = '/'+projectname+'/'
	os.mkdir(dirname)
	print "Cloning the Git repository"
	subprocess.call(["git","clone", gitlink])
	#subprocess.call(["analyst","-t", projectname,"-C","master",">","/results/#results_mockito.json"])
	print "Infer and Error Prone results to be written into results folder:" 
	runcmd = "analyst -t /"+ projectname + " -C master > /results/results_"+ projectname+".json"
	os.system(runcmd)
