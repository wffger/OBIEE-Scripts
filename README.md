# OBIEE-Scripts
## 配置文件说明
根据元素配置实际服务器及证书信息。所谓的证书就是文件化的用户名和密码。
## Powershell脚本说明 
1. 创建本地目录 
2. 备份联机存储库文件 
3. 备份共享目录
4. 复制本地目录到远程目录 
## 运行说明
直接在Powershell目录打开Poweshell窗口，然后运行“./PSxxx.ps1 ../config.xml”。配置文件相对路径作为参数传递给脚本。

## WLST脚本说明
1. 创建用户
2. 删除用户
3. 重置密码
4. 添加用户到组
5. 从组移除用户
## 运行说明
往CSV准备好数据，根据WLST.txt示例命令进入WLST，然后执行相应脚本。