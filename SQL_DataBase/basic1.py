""" DB is used to store data
RDBMS -> Relational DataBase Management System
Object oriented(django)
RDBMS--> DDL(Data Definition Language) , DML(Data Manipulation Language)
"""
"""  RDBMS"""
""" --> Table based formate 
    --> sql (mysql)-->Structured Query Language
    --> DB-->Table-->Rows&columns (Multiple tables are allowed)
    """

""" for createing db use (create database database_name)"""
""" for table creation use (create table table_name(col_name datatype)
in varchar(255) 255 is the limit of varchar"""
""" Example 
use tb;
-- create table Employee(emp_id int, emp_name varchar(250), emp_age int, emp_position varchar(250), year_of_joining datetime);
-- select * from employee;
insert into Employee(emp_id,emp_name,emp_age,emp_position,year_of_joining) values(1,"Silpamohan N",25,"junior developer","2023-09-04");
insert into Employee(emp_id,emp_name,emp_age,emp_position,year_of_joining) values(2,"Reethu Rajan",25,"junior developer","2023-09-04");
insert into Employee(emp_id,emp_name,emp_age,emp_position,year_of_joining) values(3,"Aruna Vinod",25,"junior developer","2023-09-04");
insert into Employee(emp_id,emp_name,emp_age,emp_position,year_of_joining) values(4,"Mustha",25,"junior developer","2023-09-04");
insert into Employee(emp_id,emp_name,emp_age,emp_position,year_of_joining) values(5,"Kshema",25,"junior developer","2023-09-04");
insert into Employee(emp_id,emp_name,emp_age,emp_position,year_of_joining) values(6,"Abin",25,"junior developer","2023-09-04");
select * from employee;"""