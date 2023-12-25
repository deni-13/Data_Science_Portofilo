select * from customers
select 
id,NAMESURNAME,GENDER,BIRTHDATE,CITY,TOWN
from customers

--insert into (C:\Users\secre\Documents\SQL Server Management Studio\SQLQuery2.sql)
--truncate table customers


update customers set COUNTRY='TURKÝYE',AGE=datediff(year,BIRTHDATE,getdate())

select GETDATE()


--select datediff(year,'1991-05-28','2023-12-20')


