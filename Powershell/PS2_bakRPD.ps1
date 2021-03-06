###############################
# (C) 2017 wffger 
# https://github.com/wffger
# 
# 此脚本每天备份RPD
###############################
#读入config.xml信息
param($a)
$data_xml=[xml](Get-Content $a)
$todayStrg = Get-date -format "yyyyMMdd"
$trgFldr="D:\BI-bak\"+$todayStrg+"\"
$fileNm = "BI_PROD_"+$todayStrg+".rpd"
$fileNm = $trgFldr+$fileNm
#新密码
$newPasswd = "Admin123"

$ip = $data_xml.server.ip
$port   = $data_xml.server.port
$uri = "http://${ip}:${port}/bi-lcm/v1/si/ssi/rpd/downloadrpd"

$userNm=$data_xml.server.username
$passwd=$data_xml.server.password | ConvertTo-SecureString -asPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential($userNm,$passwd)
$postParm = "target-password=${newPasswd}"

Invoke-RestMethod -Uri $uri -Method POST -Body $postParm -Credential $cred -OutFile $fileNm  

Write-Host "RPD备份成功，按任意键结束……"
$null = [System.Console]::ReadKey()