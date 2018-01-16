########################################
# (C) 2017 wffger  
# https://github.com/wffger
# 
# 此脚本根据CSV添加用户到组
########################################
import sys
from java.io import *
from weblogic.management.security.authentication import GroupEditorMBean 

print '开始脚本……'
print '此脚本将读取/home/oracle/wlst_scripts/02_user_group.csv，并将用户分配到对应组。'

csvFile = "/home/oracle/wlst_scripts/02_user_group.csv";  
cvsSplitBy = ",";

br =  BufferedReader(FileReader(csvFile));
line = br.readLine()
line = br.readLine()

atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
while line: 
	Array = line.split(cvsSplitBy);
	atnr.addMemberToGroup(Array[1],Array[0]) 
	print '成功将用户：' + Array[0] + '分配到组：' + Array[1]
	line = br.readLine()

print '结束脚本……'