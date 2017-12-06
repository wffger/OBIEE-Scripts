############################### 
# (C) 2017 wffger 
# https://github.com/wffger
# 
# 此脚本每天创建文件夹
###############################
$today = Get-date
$srcFldr="D:\BI-bak\" 
$srcFldr=$srcFldr+$today.ToString('yyyyMMdd')

New-Item -Path $srcFldr -ItemType directory -Force | out-null