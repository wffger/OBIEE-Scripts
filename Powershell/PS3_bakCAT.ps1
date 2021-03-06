############################### 
# (C) 2017 wffger 
# https://github.com/wffger
# 
# 此脚本每天备份Catalog
###############################

#读入config.xml信息
param($a)
$data_xml=[xml](Get-Content $a)

if (-not (test-path "C:\Oracle\Middleware\Oracle_Home\bi\bitools\bin")) 
{throw "找不到路径 C:\Oracle\Middleware\Oracle_Home\bi\bitools\bin，请安装OBIEE开发客户端！"} 
Set-Alias runcat "C:\Oracle\Middleware\Oracle_Home\bi\bitools\bin\runcat.cmd" 

$todayStrg = Get-date -format "yyyyMMdd"
$trgFldr="D:\BI-bak\"+$todayStrg+"\"
$fileNm = "shared_"+$todayStrg+".catalog"
$fileNm = $trgFldr+$fileNm 

$ip = $data_xml.server.ip
$port   = $data_xml.server.port
$uri = "http://${ip}:${port}/bi-lcm/v1/si/ssi/rpd/downloadrpd"
#读取证书文件相对路径
$credFile = $data_xml.credential.relativePath
 
runcat -cmd archive -online $uri -credentials $credFile -folder /shared -outputFile $fileNm

Write-Host "Catalog备份成功，按任意键结束……"
$null = [System.Console]::ReadKey()