## celery demo
### 结构说明
* celery_app 初始化创建celery实例对象、加载broker
* config broker连接信息  
* tasks 处理任务函数
* tests 单元测试

### 启动方式
进入celery_demo同级目录执行 `celery -A celery_demo worker -l info`


  