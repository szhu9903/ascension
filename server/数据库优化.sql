-- 历史轨迹表优化记录
	-- 常用筛选列 vrs_equipcode:设备编码、data_stamp:时间戳、adid:分区

-- 按设备编码筛选
select count(*) from Vehicle_ReportStatus where vrs_equipcode='16402'
-- 按时间筛选
select count(*) from Vehicle_ReportStatus where data_stamp BETWEEN '2020-09-01' and '2020-10-01'
-- 分区筛选
select count(*) from Vehicle_ReportStatus where adid=9
-- 组合查询
select count(*) from Vehicle_ReportStatus 
where data_stamp BETWEEN '2020-09-01' and '2020-10-01' and vrs_equipcode='16402' and adid=1 
/* 查询结果都在(15-30)min 之间,查询条件有 分区、时间、设备code 
adid 数据量较小，使用单独查询较少所以不创建索引，创建设备code、日期索引，
alter table Vehicle_ReportStatus add index index_vrs_equipcode(vrs_equipcode);
alter table Vehicle_ReportStatus add index index_data_stamp(data_stamp);
创建索引后组合查询、日期查询、code查询时间0.1min以内，由于adid未创建索引，adid单独查询时间在20min以上




