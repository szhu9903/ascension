--select * from t_excel 

--select * from t_excel t1
--inner join (
--select * from openquery(hxrpt,'select * from kpcbmxsj')) t2 on t1.f1=t2.wldm 

--select count(*) from openquery(hxrpt,'select * from kpcbmxsj')
--刷新开票成本表
select t1.*,t3.yjfl,t3.ejfl from (
select f1,sjfl,id as ejsl from t_excel  t1
inner join (select * from openquery(hxrpt,'select * from yjfl')) t2 on t1.f5+'-'+f6=t2.flzd
where t1.fid>=1 and t1.fid<10000) t1
inner join openquery(hxrpt,'select * from kpcbmxsj') t3 on t1.f1=t3.wldm


update t3 set yjfl=t1.sjfl,ejfl=t1.ejsl
 from (
select f1,sjfl,id as ejsl from t_excel  t1
inner join (select * from openquery(hxrpt,'select * from yjfl')) t2 on t1.f5+'-'+f6=t2.flzd
where t1.fid>=70000 and t1.fid<80000) t1
inner join openquery(hxrpt,'select * from kpcbmxsj') t3 on t1.f1=t3.wldm 

--select distinct wldm,wlmc,yjfl,ejfl from openquery(hxrpt,'select * from kpcbmxsj') 
--where isnull(yjfl,0)=0 and isnull(wldm,'')<>''


--select * from openquery(hxrpt,'select * from yjfl')

--select wldm,ejfl from openquery(hxrpt,'select * from qmjcsj')
--刷新期末结存表
select t1.*,t3.yjfl,t3.ejfl from (
select f1,sjfl,id as ejsl from t_excel  t1
inner join (select * from openquery(hxrpt,'select * from yjfl')) t2 on t1.f5+'-'+f6=t2.flzd
) t1
inner join openquery(hxrpt,'select * from qmjcsj ') t3 on t1.f1=t3.wldm
where t1.sjfl<>t3.yjfl



update t3 set yjfl=t1.sjfl
 from (
select f1,sjfl,id as ejsl from t_excel  t1
inner join (select * from openquery(hxrpt,'select * from yjfl')) t2 on t1.f5+'-'+f6=t2.flzd
 ) t1
inner join openquery(hxrpt,'select * from qmjcsj ') t3 on t1.f1=t3.wldm 
where t1.sjfl<>t3.yjfl

--1316506
--刷新呆滞品
select t1.*,t3.yjfl,t3.ejfl from (
select f1,sjfl,id as ejsl from t_excel  t1
inner join (select * from openquery(hxrpt,'select * from yjfl')) t2 on t1.f5+'-'+f6=t2.flzd
) t1
inner join openquery(hxrpt,'select * from dzpkcfxsj ') t3 on t1.f1=t3.wldm
where t1.sjfl<>t3.yjfl



update t3 set yjfl=t1.sjfl
 from (
select f1,sjfl,id as ejsl from t_excel  t1
inner join (select * from openquery(hxrpt,'select * from yjfl')) t2 on t1.f5+'-'+f6=t2.flzd
 ) t1
inner join openquery(hxrpt,'select * from dzpkcfxsj ') t3 on t1.f1=t3.wldm 
where t1.sjfl<>t3.yjfl

select distinct wldm,wlmc,yjfl,ejfl from openquery(hxrpt,'
select * from qmjcsj where ejfl is null or yjfl is null ') 
where  isnull(yjfl,0)=0 and isnull(wldm,'')<>''
union all
select distinct wldm,wlmc,yjfl,ejfl from openquery(hxrpt,'select * from kpcbmxsj 
where ejfl is null or yjfl is null') 
where isnull(yjfl,0)=0 and isnull(wldm,'')<>''
union all
select distinct wldm,wlmc,yjfl,ejfl from openquery(hxrpt,'select * from dzpkcfxsj 
where ejfl is null or yjfl is null') 
where isnull(yjfl,0)=0 and isnull(wldm,'')<>''


select  wldm,wlmc,yjfl,ejfl from openquery(hxrpt,'
select * from qmjcsj where ejfl is null or yjfl is null ') 
where  isnull(yjfl,0)=0 and isnull(wldm,'')<>'' and isnull(ejfl,0)<>0

update t2 set yjfl=t1.sjfl
--select *
from 
(select * from openquery(hxrpt,'select * from yjfl')) t1 
inner join openquery(hxrpt,'select * from qmjcsj where ejfl is null or yjfl is null') t2 on t1.id=t2.ejfl
where  isnull(yjfl,0)=0 and isnull(wldm,'')<>'' and isnull(ejfl,0)<>0

update t2 set yjfl=t1.sjfl
--select *
from 
(select * from openquery(hxrpt,'select * from yjfl')) t1 
inner join openquery(hxrpt,'select * from dzpkcfxsj where ejfl is null or yjfl is null') t2 on t1.id=t2.ejfl
where  isnull(yjfl,0)=0 and isnull(wldm,'')<>'' and isnull(ejfl,0)<>0


