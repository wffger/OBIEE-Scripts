########################################
# (C) 2017 wffger  
# https://github.com/wffger
# 
# 此脚本从CSV删除Weblogic用户
########################################
import sys
from java.io import *
from weblogic.management.security.authentication import UserEditorMBean
from weblogic.management.security.authentication import UserRemoverMBean 

print '开始脚本……'
print '此脚本将读取/home/oracle/wlst_scripts/01_user.csv，并删除相应用户。'

csvFile = "/home/oracle/wlst_scripts/01_user.csv";  
cvsSplitBy = ",";

br =  BufferedReader(FileReader(csvFile));
print br
line = br.readLine()
line = br.readLine()

print '正在删除账户 ...'
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
numFailed=0
numDeleted=0

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
		atnr.removeUser(EMPLOYEENUMBER) 
		print '用户 ' + EMPLOYEENUMBER + ' 删除成功！'
		numDeleted=numDeleted+1
		line = br.readLine()
	else: 
		print '用户 ' + EMPLOYEENUMBER + ' 不存在！'
		numFailed=numFailed+1
		line = br.readLine()

print str(numFailed) + ' 个账户不存在:)'
print str(numDeleted) + ' 个账户已删除:)'
print '结束脚本……'