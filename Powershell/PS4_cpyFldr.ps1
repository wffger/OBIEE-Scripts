############################### 
# (C) 2017 wffger 
# https://github.com/wffger
# 
# 此脚本复制文件夹到远程目录
###############################
$srcFldr="D:\BI-bak\"
$trgFldr="\\10.0.100.100\bi项目实施\备份"

$today = Get-date
$srcFldr=$srcFldr+$today.ToString('yyyyMMdd')

###############################
Write-Host "复制${srcFldr}到${trgFldr}……"
Copy-Item -recurse $srcFldr $trgFldr
Write-Host "复制完成，按回车键结束。"
$null = [System.Console]::ReadKey()