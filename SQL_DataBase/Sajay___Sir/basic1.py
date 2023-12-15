"""
workbench is a user interface
1.Mysql quaries used to interact with database

2. database: collection of database tables
    * create a new database
    * create database bookdb;  (qurery for creating badabase)
        use bookdb; (for using the database)

3.tables: collection of records(column are there  as attribute)
    * string--> varchar(limit of characters)
    * int--> int
    * boolean--> boolean
    * double-->
    * float--> float
    * date--> date
    * date time-->datetim
    * create table table_name(column_name datatype constraints);
    * insertion:
            insert into table_name(col_names)values(values);
    * fetching information
            select * from table_name;

4.constrains : auto increment(automatically increment the id),
                not null(entry is complusory),
                unique(that value appear in the table only once)--> no duplicate

5. keys: primary key(used for uniquely identify the column)
            primary key(col_name)

"""