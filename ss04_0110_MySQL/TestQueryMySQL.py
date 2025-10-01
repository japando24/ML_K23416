import mysql.connector

server = "localhost"
port = 3306
database = "studentmanagement"
username = "root"
password = "@Dnb24042004"

conn = mysql.connector.connect(
    host=server,
    port=port,
    user=username,
    password=password,
)

# #2.1. Truy van toan bo sinh vien
# cursor = conn.cursor()
#
# sql="select * from studentmanagement.student"
# cursor.execute(sql)
#
# dataset=cursor.fetchall()
# align='{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID', 'Code','Name',"Age"))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age=item[3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
#
# cursor.close()

# #2.2 Truy vấn các Sinh viên có độ tuổi từ 22 tới 26
# cursor = conn.cursor()
# sql="SELECT * FROM studentmanagement.student where Age>=22 and Age<=26"
# cursor.execute(sql)
#
# dataset=cursor.fetchall()
# align='{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID', 'Code','Name',"Age"))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age=item[3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
#
# cursor.close()

# #2.3 Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần
# cursor = conn.cursor()
# sql="SELECT * FROM studentmanagement.student " \
#     "order by Age asc"
# cursor.execute(sql)
#
# dataset=cursor.fetchall()
# align='{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID', 'Code','Name',"Age"))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age=item[3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
#
# cursor.close()
#
# #2.4 Truy vấn các Sinh viên có độ tuổi từ 22 tới 26 và sắp xếp theo tuổi giảm dần
# cursor = conn.cursor()
# sql="SELECT * FROM studentmanagement.student " \
#     "where Age>=22 and Age<=26 " \
#     "order by Age desc "
# cursor.execute(sql)
#
# dataset=cursor.fetchall()
# align='{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID', 'Code','Name',"Age"))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age=item[3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
#
# cursor.close()
#
# #2.5 Truy vấn chi tiết thông tin Sinh viên khi biết Id
# cursor = conn.cursor()
# sql="SELECT * FROM studentmanagement.student " \
#     "where ID = 1 "
#
# cursor.execute(sql)
#
# dataset=cursor.fetchone()
# if dataset!=None:
#     id,code,name,age,avatar,intro=dataset
#     print("Id=",id)
#     print("code=",code)
#     print("name=",name)
#     print("age=",age)
#
# cursor.close()
#
# #2.6 Truy vấn dạng phân trang Student
# #Lần 1: truy vấn 3 dòng dữ liệu đầu tiên
# cursor = conn.cursor()
# sql="SELECT * FROM studentmanagement.student LIMIT 3 OFFSET 0"
# cursor.execute(sql)
#
# dataset=cursor.fetchall()
# align='{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID', 'Code','Name',"Age"))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age=item[3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
#
# cursor.close()
#
# print("-"*30)
# #Lần 2: truy vấn 3 dòng dữ liệu đầu tiên
#
# cursor = conn.cursor()
# sql="SELECT * FROM studentmanagement.student LIMIT 3 OFFSET 3"
# cursor.execute(sql)
#
# dataset=cursor.fetchall()
# align='{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID', 'Code','Name',"Age"))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age=item[3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
#
# cursor.close()

# #PAGING!!!
# print("PAGING!!!!!")
# cursor = conn.cursor()
# sql="SELECT count(*) FROM studentmanagement.student"
# cursor.execute(sql)
# dataset=cursor.fetchone()
# rowcount=dataset[0]
#
# limit=3
# step=3
# for offset in range(0,rowcount,step):
#     sql=f"SELECT * FROM studentmanagement.student LIMIT {limit} OFFSET {offset}"
#     cursor.execute(sql)
#
#     dataset=cursor.fetchall()
#     align='{0:<3} {1:<6} {2:<15} {3:<10}'
#     print(align.format('ID', 'Code','Name',"Age"))
#     for item in dataset:
#         id=item[0]
#         code=item[1]
#         name=item[2]
#         age=item[3]
#         avatar=item[4]
#         intro=item[5]
#         print(align.format(id,code,name,age))
#
# cursor.close()

# #3.1 Thêm mới 1 Student
# cursor = conn.cursor()
#
# sql="insert into studentmanagement.student (code,name,age) values (%s,%s,%s)"
#
# val=("sv07","Trần Duy Thanh",45)
#
# cursor.execute(sql,val)
#
# conn.commit()
#
# print(cursor.rowcount," record inserted")
#
# cursor.close()

# #3.2 Thêm mới nhiều Student
# cursor = conn.cursor()
#
# sql="insert into studentmanagement.student (code,name,age) values (%s,%s,%s)"
#
# val=[
#     ("sv08","Trần Quyết Chiến",19),
#     ("sv09","Hồ Thắng",22),
#     ("sv10","Hoàng Hà",25),
#      ]
#
# cursor.executemany(sql,val)
#
# conn.commit()
#
# print(cursor.rowcount," record inserted")
#
# cursor.close()

# #4.1 Cập nhật tên Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà”
# cursor = conn.cursor()
# sql="update studentmanagement.student set name='Hoàng Lão Tà' where Code='sv09'"
# cursor.execute(sql)
#
# conn.commit()
#
# print(cursor.rowcount," record(s) affected")

# #4.2 Cập nhật tên Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà” như viết dạng SQL Injection
# cursor = conn.cursor()
# sql="update studentmanagement.student set name=%s where Code=%s"
# val=('Hoàng Lão Tà','sv09')
#
# cursor.execute(sql,val)
#
# conn.commit()
#
# print(cursor.rowcount," record(s) affected")

# #5.1 Xóa Student có ID=9
# conn = mysql.connector.connect(
#                 host=server,
#                 port=port,
#                 database=database,
#                 user=username,
#                 password=password)
# cursor = conn.cursor()
# sql="DELETE from studentmanagement.student where ID=9"
# cursor.execute(sql)
#
# conn.commit()
#
# print(cursor.rowcount," record(s) affected")

#5.2 Xóa Student có ID=10 với SQL Injection
conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql = "DELETE from studentmanagement.student where ID=%s"
val = (10,)

cursor.execute(sql, val)

conn.commit()

print(cursor.rowcount," record(s) affected")