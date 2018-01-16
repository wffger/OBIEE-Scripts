########################################
# (C) 2017 wffger  
# https://github.com/wffger
# 
# 此脚本根据CSV从组移除用户
########################################
import sys
from java.io import *
from weblogic.management.security.authentication import GroupEditorMBean

operDesc = '从组移除用户'
print '开始脚本……'
print '此脚本将读取/home/oracle/wlst_scripts/02_user_group.csv，并'+operDesc+'。'

csvFile = "/home/oracle/wlst_scripts/02_user_group.csv";  
cvsSplitBy = ",";

br =  BufferedReader(FileReader(csvFile));
line = br.readLine()
line = br.readLine()

print '正在'+operDesc+'...'
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
numCreated=0
numIgnored=0

while line: 
	Array = line.split(cvsSplitBy);
	member 	=	Array[0]
	groupName	=	Array[1]
	if not atnr.userExists(member):
		print '用户 ' + member + ' 不存在！'
		numIgnored=numIgnored+1
		line = br.readLine()
	else:
		atnr.removeMemberFromGroup(groupName,member)
		print member+' 操作成功.'
		numCreated=numCreated+1
		line = br.readLine()

print str(numCreated) + ' 个操作成功。'
print str(numIgnored) + ' 个操作忽略。'
print '结束脚本……'