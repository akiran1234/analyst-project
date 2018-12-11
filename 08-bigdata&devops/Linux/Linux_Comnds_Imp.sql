
#########################Linux Process Management Commands #########################################
top                # will list out the top running process
sudo netstat -tulp # To check the open ports in linux and process id and service open to that port.
                      # -tulp: tcp,udp,list,ports
                   
######################### Forward and Background Process ############################################
nohup cmd/script &  # This will run the command or script in background as a process. Using "nohup" will ensure to run as a process even the session is closed.
sleep 20 &                    # This will run the sleep command is background for 20 sec.
jobs                                # Will list the background running process. Each process is called Job starting with numbers 1,2 ...
fg jobid                          # Will bring the background running process to forground.
fg 3                                 # This will bring 3 job to foreground.

sleep 40                        # This command is running and shell prompt is blocked for further usage. ctrl+z will stop the process
jobs                               # This will list the jobid of the stopped process
bg jobid                        # This will run the stopped process as a background process.

######################### File System Commands ############################################  
du -sh                            # This will display the size of a directory usage.                
lsblk                               # Will list all the partitions of block storage. It will list all drives attached to linux machine.
df -h                              # Will display mounted file systems usage.
df -h | grep ^/dev      # Will display the disk partions usage.
ifconfig # ip address
######################### ############################################

hostname -i                # Dispalys IP Address
hostname -I                # Dispalys IP Address
ip address show        # Dispalys IP Address
type command         # Will tell it is builtin shell command/package installed in /usr/bin/
sudo service tomcat status   # to check the status of a service 
sudo systemctl status tomcat # to check the status of a service 
ps -ef                           # To check all running process id.

###################### Default File Permission #####################
By default files will have 666(files) and directories will have 777(dir) permision
umask =022               # Based on umask the file permissions will be set default umask is 002 however this can be changed from /etc/login.defs
file-666
   - 022
--------------------
     644(Default)        # File Permissions
---------------------
dir-777
  - 022
---------------------	   
    745(Default)          # Directory Permissions.
---------------------	
###################### Cron Jobs #####################
crontab -l                   # To view the list of cron jobs that is been scheduled to run.
crontab -e                  # This will open a file where we need to give the time and path of the script to be executed.
cronjob formate      # (mins) (hrs) (days) (months) (weekoftheday)
Make sure the script that has to be executed has 755 permissions.
################# How to Change hostname Centos ###################
cat /etc/hostname                   # It will show the hostname of the machine
cat /etc/sysconfig/network   # It will show the hostname of the machine
hostnamectl                               # This will display the complete hostname details
hostnamectl set-hostname <new-hostname> # It will rename the hostname, login with new session execute the above commands and ensure it is changed

################ How to create hostname entry in internal DNS Lookup ###########
cat /etc/hosts                           # Internal DNS Look up if hostname is reachable by ping.

127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
127.0.0.1   www.kiran.com kirana # This is an internal DNS Lookup, checking if hostname 2nd col and alias name 3rd col reaches.
10.0.2.15    achanta                          # Added hostname in internal DNS Lookup
10.0.2.15    testing                            # Same IP with different identifier name
######## Zombie vs Orpahan ############################
Fork: fork is an operation whereby a process creates a copy of itself. It is usually a system call, implemented in the kernel. 
Let say there is Parent(p1) and Child Process(p2), now parent has terminated(p1) with out waiting for its child process(p2) and child becomes orphan i.e p2.
Let say there is Parent(p3) and Child Process(p4), now Child has terminated(p4) before its parent process(p3) has terminated here p4 entry is not removed from process table until p3 terminates.
Now p4 becomes Zombie.





