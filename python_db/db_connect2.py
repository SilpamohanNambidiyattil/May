import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="Password@123",database="animal")
cursor=db.cursor()
# create a table buffalo
# id age weight bread image
query="create table buffalol(id int auto_increment primary key, age int not null)"
cursor.execute(query)


