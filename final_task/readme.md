# 爬取51job上python工程师的薪资并求北京地区python开发者平均薪资

+ dbutil：包含两文件`config.py`和`database.py`，功能为封装数据库操作；
  + config.py：数据库配置文件
  + database.py：数据库ORM模型及操作封装
+ spider.py：封装了爬虫操作，调用了database模块中的数据库存入功能
+ main.py：启动爬虫
+ get_avg.py：求得北京地区python开发者薪资水平（单位万/月）
+ webspider.sql：数据库文件