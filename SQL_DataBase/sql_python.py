import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Silpamohan@97",port=3306)
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("create database python")
mycursor.execute("use python")
# mycursor.execute("create table student(name varchar(255),roll_number int,age int)")
sql="insert into student(name,roll_number,age) values(%s,%s,%s)"
# val=("silpa","1","25")
# val=("reethu","2","27")
# val=("aruna","3","24")
# val=("mustha","4","25")
mycursor.execute(sql,val)
mydb.commit()