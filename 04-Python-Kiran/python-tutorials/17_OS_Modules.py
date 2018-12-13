import os

#print("os.system('pwd'): Linux command from python",os.system('pwd'))
print("os.environ: Print environmental variables",   os.environ)
print("os.getcwd():Print current working dir",       os.getcwd())
#print("os.getuid():Print user id",                  os.getuid())
#print("os.uname() :Print user name",                os.uname())

print("os.path:Print the path of python lib:",       os.path)
# os.mkdir("newdir")
# os.chdir("newdir")
# os.getcwd()
# os.rmdir('dirname')

print("**********************")

import os
hostname = "8.8.8.8"                     # google dns ip address
response = os.system("ping " + hostname)

print("Printing the response=",response) # response=0 for reachable; response=1 for not reachable.

if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')

