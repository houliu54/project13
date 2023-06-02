"""
验证SQL注入
"""
from mysql import connector
from pymysql import connect

con = connect(host='localhost',port=3306,user='root',passwd='root',database='tt')
cursor = con.cursor()

# sql = "select * from tester where user_name='张三'#'and age='11111'"
sql = "select * from tester where user_name='张三'-- 'and age='11111'"
insert_sql = "insert into tester(user_name) values(%s)"
cursor.executemany(insert_sql,['a','b','c'])

con.commit()
#
# results = cursor.fetchall()
# # print(type(results))
# for i in results:
#     print(i)

cursor.close()
con.close()
