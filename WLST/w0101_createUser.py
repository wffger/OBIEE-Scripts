########################################
# (C) 2017 wffger  
# https://github.com/wffger
# 
# 此脚本从CSV创建Weblogic用户
########################################
import sys
from java.io import *
from weblogic.management.security.authentication import UserEditorMBean
from weblogic.management.security.authentication import UserAttributeEditorMBean 

print '开始脚本……'
print '此脚本将读取/home/oracle/wlst_scripts/01_user.csv，并创建相应用户。'

csvFile = "/home/oracle/wlst_scripts/01_user.csv";  
cvsSplitBy = ",";

br =  BufferedReader(FileReader(csvFile));
line = br.readLine()
line = br.readLine()

print '正在创建账户 ...'
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
		print '用户 ' + EMPLOYEENUMBER + ' 已经存在！'
		numIgnored=numIgnored+1
		line = br.readLine()
	else:
		atnr.createUser(EMPLOYEENUMBER,PAGER,DISPLAYNAME+'-'+DEPARTMENTNUMBER+'-'+TITLE)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'c',C)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'departmentnumber',DEPARTMENTNUMBER)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'displayname',DISPLAYNAME)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'employeenumber',EMPLOYEENUMBER)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'employeetype',EMPLOYEETYPE)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'homepostaladdress',HOMEPOSTALADDRESS)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'l',L)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'mail',MAIL)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'mobile',MOBILE)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'title',TITLE)
		atnr.setUserAttributeValue(EMPLOYEENUMBER,'preferredlanguage','Chinese')
		print EMPLOYEENUMBER+' 已创建.'
		numCreated=numCreated+1
		line = br.readLine()

print str(numCreated) + ' 个账户已创建:)'
print str(numIgnored) + ' 个操作已忽略:)'
print '结束脚本……'