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
4. 常用数据类型：
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
    >- 数据库内置数据库
    	>>- information_schema：  
    		TABLESb表：存放所有mysql数据表信息，可根据数据库名筛选，包含数据列数、数据表数据空间、索引空间等
    		EVENTS表：存放MySQL的事件（定时任务）
    		COLUMNS表：查询数据库列名：  
    			select TABLE_NAME,GROUP_CONCAT(COLUMN_NAME SEPARATOR ',') from information_schema.COLUMNS
    			where TABLE_SCHEMA='erpdb' group by TABLE_NAME
7. 数据表数据操作
	>- 删除表中数据
		>>- 删除表中所有数据 ： truncate table table_name(删除所有、立即释放磁盘空间、不支持数据回滚、删除速度快);
		>>- 删除部分数据 ： delete from table_name where column=... (按条件删除数据、不会立即释放磁盘空间、可回滚)  
			delete后释放空间 ： optimize table table_name(释放磁盘空间);
8. 约束
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
	>- 级联类型 (InnoDB)
		>>- CASCADE : 从父表中删除或更新对应行，同时自动删除或更新自表中匹配的行 ON (DELETE|UPDATE) CASCADE
		>>- SET NULL : 从父表删除或更新对应行，同时将自表对应的外键更新为NULL 列不能含有非空约束 ON (DELETE|UPDATE) SET NULL
		>>- NO ACTION : innodb 拒绝删除更新父表
		>>- RESTRICT : 同（NO ACTION）
9. MYSQL 内置函数使用
	>- 时间
		>>- NOW():当前日期时间、CURDATE():当前日期、CURTIME():当前时间
		>>- datediff : 计算时间差，DATEDIFF(expr1,expr2) 只能计算相差天数
		>>- timestampdiff : 计算时间差，TIMESTAMPDIFF(unit,小的时间,大的时间),可指定计算时差单位 天（DAY）小时（HOUR）分钟（MINUTE）秒（SECODE）
		>>- date_add(date:合法的日期表达式, interval 添加的时间间隔 type:时、分、秒) : date_add('2018-06-26',INTERVAL '5' day)
		>>- date_sub(date:合法的日期表达式, interval 添加的时间间隔 type:时、分、秒) : 减掉一段时间
	>- 查询
		>>- 去重查询 `distinct` 
		>>- 区分大小写 `binary   distinct binary`
		>>- 大小写转换 `lower()`: 转小写 `upper()`：转大写。
		>>- 过滤分组 `select name,avg(num) from user group by name having avg(num)>5`;  获取名称分组后 num平均值大于某数值
		>>- 正则表达式 `regexp`
		>>- 从一张表复制数据到另一张表 `insert into user2(fname,fage,fphone) select name,age,phone from user1`
		>>- 快速删除表中数据 `truncate table`;
		>>- 字段拼接 `concat(str1, str2)`
		>>- 指定分隔符字段拼接 `CONCAT_WS(separator,str1,str2,...)`
		>>- 分组查询列汇总 `select GROUP_CONCAT（查询的字段 separator ‘；’） from table group by 列字段`;
		>>- 获取查询数据的长度 `select length(name) from user`  
		>>- 字符串替换 `select REPLACE(str, from_str, to_str)`  
		>>- 字符串切片 `select SUBSTRING_INDEX(str, delim, count)` 
		>>- 分组数据添加汇总行 with rollup : `select name,sum(number) from table1 group by name with rollup`;
		>>- 类型转换 `CAST(expr AS type)`:`signed`:整数;`unsigned`:无符号整数;`char()`:字符型;`decimal`:浮点数  
			类似类型转换函数 `convert(value, type)`
		>>- 数字格式化操作：`truncate(value,number)`:函数会将小数部分2位以后的值直接舍去  
			`ROUND(value,number)`:小数部分四舍五入
			`format(value,number)`:小数部分四舍五入，整数部分从右向左每3位一个逗号进行格式化输出。
		>>- 三元运算 `IF(a=b, 'YES', 'NO')`
	>- 错误定义
	    >>- signal sqlstate 'HY000' set message_text = 'exeption message' (使用在触发器对数据进行业务校验)
10. MYSQL 高级
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
		>>- 创建定时任务
			DROP EVENT if EXISTS day_delup;  
			CREATE EVENT day_delup  
			ON SCHEDULE EVERY 1 DAY STARTS DATE_ADD(DATE_ADD(CURDATE(),INTERVAL 1 DAY), INTERVAL 2 HOUR)  
			ON COMPLETION PRESERVE   
			COMMENT '上行del' DO  
			BEGIN  
				delete from UpStream_Message WHERE data_stamp<=DATE_SUB(CURDATE(), INTERVAL 60 DAY);  
			END;  
11. 查询记录
	>- 分组查询每组最新一条数据
		>>- limit 1000000:在临时表内部排序时用limit字段固定排序， 然后在临时表外分组就可以改变group by默认排序（id）的问题
		>>- select * from (select * from SCO_Bill ORDER BY scob_idletime desc limit 1000000) d GROUP BY d.scob_vehicleid ;
	>- 数据每组生成编号
		>>- @r 临时变量初始化0之后adid同组的每条+1  
			@r 初始化分组标志，赋值分组标志
		>>- select @r:=case when @adid=a.adid then @r+1 else 1 end as fid, a.\*, @adid:=a.adid as l_adid
			from Vehicle_Queue_V a,(SELECT @r:=0,@adid:=0) b   
	>- 查询数据按照逗号拆分后，一行转多行   
		>>- 获取要拆分字符串包含的逗号数量   
			select length(queuedata)-length(replace(queuedata, ',', '')) from Vehicle_Queue
		>>- SUBSTRING_INDEX(SUBSTRING_INDEX(a.vq_queuedata, ',', help_topic_id+1), ',', -1)  
			累加拆分然后获取追后一个元素 即对应的元素 ,例： 180, 110, 120  
			180 --> 180  
			180,110 --> 110
			180,110,120 --> 120
		>>- 语句示例
			select 
				a.vq_producestationid,
				SUBSTRING_INDEX(SUBSTRING_INDEX(a.vq_queuedata, ',', help_topic_id+1), ',', -1)
			from Vehicle_Queue a
			JOIN mysql.help_topic b on b.help_topic_id < (LENGTH(a.vq_queuedata) - LENGTH(REPLACE(a.vq_queuedata, ',', ''))+1)
	>- 分组查询数据 组转列
		>>- 例如根据饭补申请数据表统计每月汇总信息 字段： 用户、时间、饭补类型(早、中、晚)、金额  
			效果转换————>用户、时间、早count、中count、晚count、总金额
		>>- SQL语句示例
			select 
				a.ds_signuserid, -- 用户
				a.group_date, -- 日期
				SUM(a.ds_fee) as ds_fee, -- 总金额
				SUM(CASE WHEN a.ds_riceitem='BREAKFAST' THEN a.ds_count ELSE 0 END) as ds_breakfast, -- 统计早餐条件，其他为0
				SUM(CASE WHEN a.ds_riceitem='LUNCK' THEN a.ds_count ELSE 0 END) as ds_lunck, -- 统计午餐条件，其他为0
				SUM(CASE WHEN a.ds_riceitem='DINNER' THEN a.ds_count ELSE 0 END) as ds_dinner -- 统计晚餐条件，其他为0
			FROM
			(
			-- 按月分组所有类型次数，详细分组	
			select 
				ds_signuserid,
				DATE_FORMAT(ds_signdatetime, '%Y-%m') as group_date,
				ds_riceitem,
				sum(ds_fee) as ds_fee,
				count(\*) as ds_count
			from Driver_Subrice 
			GROUP BY ds_signuserid, DATE_FORMAT(ds_signdatetime,'%Y%m'),ds_riceitem) a
			GROUP BY ds_signuserid, group_date

12. 配置问题处理
	>- 创建触发器语句较长时,数据库错误：Lost connection to MySQL server during query
		原因： 实际问题是因为导入的文件大小大于mysql默认的数据包限制大小4M
		查看：show variables like '%max_allowed_packet%'
		解决：打开my.ini配置文件，设置：max_allowed_packet = 500M 重启
	>- 重启web服务时，数据库错误：1040, 'Too many connections'
		原因：MySql的最大连接数量，先检查是否为程序重启未释放数据库连接
		查看：show variables like '%max_connections%';
		解决：打开my.ini配置文件，设置：max_connections = 800 
