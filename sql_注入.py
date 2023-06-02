"""
验证SQL注入
"""
from mysql import connector
from pymysql import connect
# 创建连接，连接到sql服务
con = connect(host='localhost',port=3306,user='root',passwd='root',database='tt')
cursor = con.cursor() # 创建游标

# sql = "select * from tester where user_name='张三'#'and age='11111'"
sql = "select * from tester where user_name='张三'-- 'and age='11111'"
insert_sql = "insert into tester(user_name) values(%s)"
cursor.executemany(insert_sql,['a','b','c'])

con.commit() # 执行更新操作后需要提交
#
# results = cursor.fetchall()
# # print(type(results))
# for i in results:
#     print(i)

cursor.close() # 关闭游标
con.close() # 关闭数据库连接
