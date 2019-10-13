## python 连接mysql进行常规增删查改操作
## 与sqlyog等视图工具区别在于，python连接数据库，获取数据库游标，操作游标间接操作数据库
## 对数据库有改动（删改更新等操作）需要提交事务 commit，此处类似git

# 1：连接数据库 (四个关键字参数host,user, passwd,db,port）

# import pymysql
#
# connert = pymysql.connect(host='localhost',
#                           user='lu',
#                           passwd='123456',
#                           db='sql01',
#                           port=3308)
# # 2 ：获取游标
#
# cursor = connert.cursor()

#3:执行sql语句  ,executemany 执行多条(如批量增加）
#单表查
#sql = 'select * from lianxi01'
#简单多表查，首先确保连接的数据库存在两张表
#sql = 'select *  from lianxi01 ,hahahh where lianxi01.id = hahahh.id'
#内连接多表查询 即求两表合集
#sql = 'select *  from lianxi01 inner join hahahh on lianxi01.id = hahahh.id'
# 左右连接
#sql = 'select *  from lianxi01 left join hahahh on lianxi01.id = hahahh.id'
# 内连接 full join  mysql union  左右连接相加，
#sql = 'select *  from lianxi01 left join hahahh on lianxi01.id = hahahh.id\
#       union\
#        select *  from lianxi01 right join hahahh on lianxi01.id = hahahh.id'
# 两张以上表连接
#sql  = 'select *  from lianxi01 ' \
#       'left join hahahh ' \
#       'left join xx table ' \
#       'on lianxi01.id = hahahh.id = xxx'




### 增加
#单条数据增加
#sql = 'insert into lianxi01 value (%s,%s,%s,)',()
#批量增加数据  用executemany 两个参数，sql语句，值
#l=[('125', '张三', '1255'),('126', '张三', '1255'),('127', '张三', '1255'),]
#sql = 'insert into lianxi01 value (%s,%s,%s)'




# 删除 ！！！一定要加where啊！！
#sql = 'delete from lianxi01 where id >20'
#count = cursor.executemany(sql,l)




# 修改
# sql =  "UPDATE lianxi01 SET money = 52 WHERE id = 2"
# count = cursor.execute(sql)  #此处返回查询到的数量
# fetch = cursor.fetchall()  #fetchall 获取全部，此外还有fetchone 获取一条 fetchmany 获取多条
# print(count)
# print(fetch)
#
# connert.commit()


##至此，，数据库基础已结束

import json
import time
dicts = {"info":[{"key":"col1","value":"13646"},{"key":"col2","value":"luyinbin"},{"key":"col3","value":"06116919"}],"code":"ty"}

d = json.dumps(dicts)
session=1559568932436&url=https://ksv-video-publish.cdn.bcebos.com/128cb1f32345aae70c3ac4d1ef02bac00e55e337.mp4?auth_key=1559603523-0-0-bba160e92d8c0bc3161ab99bb0c6319b&sendTime=2019-06-03%2022:56:34
code=ty&t=1559573784301.0.18940062555458792

print(time.time())