########################################
# (C) 2017 wffger  
# https://github.com/wffger
# 
# 此脚本从CSV重置Weblogic用户密码
########################################
import sys
from java.io import *
from weblogic.management.security.authentication import UserEditorMBean
from weblogic.management.security.authentication import UserPasswordEditorMBean 

print '开始脚本……'
print '此脚本将读取/home/oracle/wlst_scripts/01_user.csv，并重置用户密码。'

csvFile = "/home/oracle/wlst_scripts/01_user.csv";  
cvsSplitBy = ",";

br =  BufferedReader(FileReader(csvFile));
print br
line = br.readLine()
line = br.readLine()

print '正在重置用户密码 ...'
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
numCreated=0
numIgnored=0

while line: 
	Array = line.split(cvsSplitBy);
	C	=	Array[0]
	DEPARTMENTNUMBER	=	Array[1]
	DISPLAYNAME	=	Array[2]
	EMPLOYEENUMBER	=	Array[3]
	EMPLOYEETYPE	=	Array[4]
	FACSIMILETELEPHONENUMBER	=	Array[5]
	GIVENNAME	=	Array[6]
	HOMEPHONE	=	Array[7]
	HOMEPOSTALADDRESS	=	Array[8]
	L	=	Array[9]
	MAIL	=	Array[10]
	MOBILE	=	Array[11]
	PAGER	=	Array[12]
	POSTALADDRESS	=	Array[13]
	POSTOFFICEBOX	=	Array[14]
	PREFERREDLANGUAGE	=	Array[15]
	ST	=	Array[16]
	STREET	=	Array[17]
	TELEPHONENUMBER	=	Array[18]
	TITLE	=	Array[19]
	if atnr.userExists(EMPLOYEENUMBER):
		atnr.resetUserPassword(EMPLOYEENUMBER,PAGER)
		print EMPLOYEENUMBER+' 操作成功.'
		numCreated=numCreated+1
		line = br.readLine()
	else: 
		print '用户 ' + EMPLOYEENUMBER + ' 不存在！'
		numFailed=numFailed+1
		line = br.readLine()

print str(numCreated) + ' 个操作成功。'
print str(numIgnored) + ' 个操作忽略。'
print '结束脚本……'