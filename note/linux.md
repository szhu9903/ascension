
# linux命令

1. 网络
	>- 查看ip: ifconfig
	>- 开放的端口
		>>- lsof -i:端口号 
		>>- netstat -anp|grep 端口号 (-a:列出所有连接状态  
			-n列出主机名和服务名  
			-p:列出pid   
			-t:所有tcp协议  
			-u:所有udp协议  
			列出所有netstat -a)
		>>- telnet 47.102.40.50 22 查看远程ssh是否开放
2. 文件
	>- zip文件操作
		压缩：zip -r new_file.zip new_file(目录)
		解压：unzip -d /解压到目录 new_file.zip
	>- tar文件操作
		打包成tar.gz格式压缩包
		tar -zcvf renwolesshel.tar.gz /renwolesshel
		解压tar.gz格式压缩包
		tar zxvf renwolesshel.tar.gz
3. 进程
	>- 进程树展示进程：pstree -ap|grep nginx
	>- 显示某进程信息：ps -ef|grep nginx

