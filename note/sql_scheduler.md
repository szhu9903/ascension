Mysql事件

查看事件调度器开启状态
	SHOW VARIABLES LIKE 'event_scheduler';
开启关闭事件调度器
	全局修改 SET GLOBAL event_scheduler = NO; 开启，OFF：关闭
	始终开启 配置文件my.ini（Windows系统）/my.cnf（Linux系统）
		event_scheduler = NO

创建事件
	CREATE 
		EVENT event_name
		ON SCHEDULE schedule --定义执行时间和时间间隔
		[ON COMPLETION [NOT] PRESERVE] -- 是否永久执行，默认一次执行：NOT PRESERVE
		[COMMENT '注释']
		DO event_body; -- 要定时执行的代码。

	ON SCHEDULE 常用时间间隔：
		EVERY子句：用于表示事件在指定时间区间内每隔多长时间发生一次,1 DAY：每天，1 MONTH：每月
		interval：表示一个从现在开始的时间，其值由一个数值和单位构成。例如，使用“4 WEEK”表示4周；使用“‘1:10’ HOUR_MINUTE”表示1小时10分钟。间隔的距离用DATE_ADD()函数来支配。
		每隔5秒执行：ON SCHEDULE every 5 second[YEAR | QUARTER | MONTH | DAY | HOUR | MINUTE |
			WEEK | SECOND | YEAR_MONTH | DAY_HOUR | DAY_MINUTE |
			DAY_SECOND | HOUR_MINUTE | HOUR_SECOND | MINUTE_SECOND];
		每天凌晨1点执行 ： ON SCHEDULE every 1 DAY starts DATE_ADD(DATE_ADD(CURDATE(), INTERVAL 1 DAY), INTERVAL 1 HOUR)
		每月第一天凌晨1点 ： 
			select DATE_ADD(DATE_ADD(DATE_SUB(CURDATE(),INTERVAL DAY(CURDATE())-1 DAY),INTERVAL 1 MONTH),INTERVAL 1 HOUR)
查询事件
	SELECT * from information_schema.EVENTS
启动与关闭事件
	启动：ALTER EVENT event_name ENABLE;
	关闭：ALTER EVENT event_name DISABLE;
删除事件
	drop EVENT if exists event_name;



