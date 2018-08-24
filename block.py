import commands
from datetime import datetime

t1=datetime.now()

### A Input is Active and D Input is deactivate (self script) ###

ip=raw_input('Enter The Ip Address')
output = commands.getoutput('iptables -A INPUT -s %s -j DROP' %ip)

#print output

t2=datetime.now()

print t2-t1



##### Notes: its work in linux.(kali) when you deactivate then select ine no: "9" and replace "A" to "D" ####
