import psycopg2

'''
# 连接数据库
conn = psycopg2.connect(database="testdb",user="postgres",
                        password="1017",host="127.0.0.1",port="5432")
print('Opened database successfully')

# 创建表
cur = conn.cursor()
cur.execute("""create table student
    (ID int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary real)""")
print('table created successfully')

conn.commit()
conn.close()
'''


# 插入数据
'''
conn = psycopg2.connect(database="testdb",user="postgres",
                        password="1017",host="127.0.0.1",port="5432")

cur = conn.cursor()
cur.execute("insert into student(id,names,address) values(7,'臣','嘉兴')");
conn.commit()
conn.close()
'''

print('9测试')

# 查
import time
conn = psycopg2.connect(database="testdb",user="postgres",password="1017",host="127.0.0.1",port="5432")
cur = conn.cursor()
cur.execute("select id,names,address from student")
rows = cur.fetchall()
for row in rows:
    time.sleep(3)
    print("id = %s \n name = %s \n address = %s"%(row[0],row[1],row[2]))
print('Operation done successfully')
conn.close()










