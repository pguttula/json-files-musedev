# Below script requires two command line arguments: project name and git link
# use - python musedevrun.py projectname GitHublink

import os
import sys
import subprocess


projectname = str(sys.argv[1])
gitlink = str(sys.argv[2])
subprocess.call(["rm","-rf", projectname])
dirname = '/'+projectname+'/'
os.mkdir(dirname)
print "Cloning the Git repository"
subprocess.call(["git","clone", gitlink])
#subprocess.call(["analyst","-t", projectname,"-C","master",">","/results/#results_mockito.json"])
print "Infer and Error Prone results to be written into results folder:" 
runcmd = "analyst -t /"+ projectname + " -C master > /results/results_"+ projectname+".json"
os.system(runcmd)
