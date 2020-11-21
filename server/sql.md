# MYSQL

1. 数据库服务
	>- 启动MySQL数据库服务：net start mysql
	>- 停止MySQL数据库服务：net stop mysql
2. MySQL系统信息
	>- 查看版本信息：status
	>- 查看数据库文件位置：show variables like 'datadir';
3. 常用数据库命令
	>- 登录mysql ： mysql -u root -p
	>- 显示数据库列表 ： show databases
	>- 创建数据库 ： create database db_name  
	创建数据库防止重名报错：create database if not exists db_name
	>- 删除数据库 : drop database db_name
	>- 跳转到数据库 ： use db_name
4. 常用数据表操作：
	>- 浮点数类型：float(单精度浮点数） double(双精度浮点数)  decimal(10，0)
	>- 时间类型：year、time、date、datetime、timestamp(时区)
	>- 字符串类型：char(m：固定长度字符串)  varchar(m:固定长度不满足是 自动删除空格)  text(文章评论 非二进制)
		enum('val1','val2',val3:自动创建索引null or 0：)
	>- 二进制类型：blob(常用存储图片文件)
5. 数据库引擎：
	>- 主要数据库存储引擎:innodb(支持外键事务处理的存储引擎)，myisam(主要的非事务处理存储引擎)
	>- 查看数据库引擎：show variables like 'default_storage_engine%';
	>- 修改数据库引擎：set default_storage_engine=<数据库引擎名称(inbodb\myisam)>
6. 数据表操作
	>- 创建表：CREATE TABLE tb_emp1(
    	id INT(11),
    	name VARCHAR(25),
    	deptId INT(11),
    	salary FLOAT);
    >- 删除数据表：drop table <表名>；
    >- 删除有外键的数据表：alter table temp2 drop foregin key fk_emp1; drop table temp1
    >- 修改表名：alter table <旧表名> rename to <新表名>；
    >- 修改表字符集：alter table <表名> character set 'gb2312(字符集名称)' collate 校对规则名;
    >- 查看表信息：show create table <表名>；
    >- 查看表字段说明：desc <表名>；
    >- 修改表中字段名：alter table <表名> change <旧列名> <新列名> <新数据类型>；
    >- 修改字段数据类型：alter table <表名> modify <列名> <新数据类型>;
    >- 删除数据列：alter table <表名> drop <列名>;
    >- 添加列：alter table <表名> add <列名><数据类型>[约束]；（默认添加最后）
    	alter table user add new_l int(4) first;(添加到开始位置)  
    	alter table user add new_l int(4) after name; (添加到指定列之后)  
7. 约束
	>- 主键约束（primary key）  
		>>- 定义字段时创建主键索引：（ID int(4) primary key）,
	 	>>- 定义完所有字段时：（constraint primary key id）
		>>- 添加主键约束： alter table user add primary key (id);
		>>- 删除主键约束： alter table user drop primary key;
		>>- 创建自增主键索引：create table test(
			id int(4) primary key aotu_increment,
			name varchar(23)
			);
	>- 外键约束 (foreign key)
		>>- 创建外键约束：create table temp1(
			id int(11) primary key,
			name varchar(25));
			create table temp2(
			id int(11) primary key,
			name varchar(20),
			dept_id int(11),
			constraint fk_temp1 foreign key (dept_id) references temp1(id)
			) ;
		>>- 修改表创建外键约束：alter table 表名 add constraint 外键名 foreign key (字段名) references 关联表（id）
		>>- 删除外键约束: alter table 表名 drop foreign   外键名
	>- 唯一约束 (unique key) 
		>>- 创建唯一约束： 字段名 类型 unique,
		>>- 修改表创建唯一约束：alter table user add constraint unique(字段名) 
		>>- 删除唯一索引Lalter table user drop index 字段名
	>- 检查约束（check）
		>>- 修改表添加检查约束：alter table user add constraint check_ssi check(ssi>0 and ssi<10);
		>>- 删除检查约束：alter table user drop constraint check_ssi;
	>- 默认值约束(default)
		>>- 修改表时添加默认值约束：alter table user change column name name varchar(20) defaule 'test';
		>>- 删除默认值约束：alter table user change column name name varchar(21) default NULL;
	>- 非空约束（not null）
		>>- 修改表添加非空约束：alter table user change column name name varchar(21) not NULL;
		>>- 删除非空约束：alter table user change column name name varchar(21) NULL;
8. MYSQL 内置函数使用
	>- 时间
		>>- datediff : 计算时间差，DATEDIFF(expr1,expr2) 只能计算相差天数
		>>- timestampdiff : 计算时间差，TIMESTAMPDIFF(unit,小的时间,大的时间),可指定计算时差单位 天（DAY）小时（HOUR）分钟（MINUTE）秒（SECODE）
	>- 查询
		>>- 去重查询 distinct 
		>>- 区分大小写 binary   distinct binary
		>>- 过滤分组 select name,avg(num) from user group by name having avg(num)>5;  获取名称分组后 num平均值大于某数值
		>>- 正则表达式 regexp
		>>- 从一张表复制数据到另一张表 insert into user2(fname,fage,fphone) select name,age,phone from user1
		>>- 快速删除表中数据 truncate table;
9. MYSQL 高级
	>- sql视图
		>>- 创建视图 create view 视图名称 as select 语句；
		>>- 删除视图 drop view 视图名称；
		>>- 创建或修改视图 create or replace view 视图名称 as 视图内容；
	>- 索引 
		>>- 创建表时：create table user(
			id bigint(20) primary key auto_increment,
			column1 varchar(10),
			column2 varchar(10)
			index(column1,column2)
		);
		>>- 添加索引： create index 索引名 on 表名 (column1);
		>>- 修改表时增加索引： alter table 表名 add index 索引名(索引字段名);
		>>- 组合索引：遵循最左前缀 column1  column1,column2 
	>- 触发器 
		>>- 创建触发器
		drop trigger if EXISTS [trigger_name];
		DELIMITER ||
		create trigger [trigger_name] 
		[after|before] [insert|update|delete] on [table_name] for each row
		begin 
			IF(old.he_name != new.he_name) or (old.he_type != new.he_type)
			THEN
					set new.he_icid=old.icid + 1; 
			end IF;
		end
		||
		DELIMITER ;
	>- 存储过程
		>>- 创建函数
			-- delimiter 用在命令行，非命令行，不需要结尾delimiter;   
			delimiter //  
			-- 如果存在旧的存储过程，删除旧的存储过程，  
			DROP PROCEDURE IF EXISTS insert_icid;  
			-- 传递参数 in param_name param_type,  
			CREATE PROCEDURE insert_icid(in startphone varchar(50))  
			BEGIN  
				DECLARE num INT default 0;  
				WHILE num<10 DO  
				BEGIN  
					-- concat : 字符串拼接  
					-- floor : 向下取整 3.69->3  
					-- rand : 获取0-1随机数  
					INSERT INTO Sys_Iccard (si_cardnum, si_phonenum)   
					values(CONCAT('55694266987125658', FLOOR(RAND() * 1000)), CONCAT(startphone, FLOOR(RAND() * 10000)));  
				END;  
				END WHILE;  
			select * from sys_iccard order by id desc limit 50;  
			END;  
			// delimiter;  
		>>- 调用函数
			call procedure_name('15994092160')